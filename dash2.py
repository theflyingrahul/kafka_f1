from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, DoubleVar

import threading
from time import sleep

from confluent_kafka import Consumer
from confluent_kafka import KafkaError, KafkaException
import sys
import socket


distance_per_lap = 6000
total_lap = 5

# Kafka stuff
consumer_poll_duration = 1

conf = {'bootstrap.servers': '172.16.100.97:9092',
        'default.topic.config': {'api.version.request': True},
        'security.protocol': 'PLAINTEXT',
        'client.id': socket.gethostname(),
        'group.id': 'dashboard',
        'enable.auto.commit':'false',
        'auto.offset.reset': 'latest'}

# Boilerplate for Kafka consumer functions
def redbull_distance():
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe(["redbull_distance"])

    try:
        while True:
            msg = consumer.poll(consumer_poll_duration)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f'Error while consuming: {msg.error()}')
            else:
                # Parse the received message
                value = msg.value().decode('utf-8')
                lap = value.split()[2]
                dist = value.split()[4]
                race_completion = ((distance_per_lap*(float(lap)) + float(dist.rstrip("m")))/(distance_per_lap*total_lap)) * 100

                canvas.itemconfig(tagOrId=rb_lap_label, text=lap)
                canvas.itemconfig(tagOrId=rb_dist_label, text=dist)
                canvas.itemconfig(tagOrId=rb_percent_label, text="{:.0f}%".format(race_completion))


    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()


def mercedes_distance():
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe(["mercedes_distance"])

    try:
        while True:
            msg = consumer.poll(consumer_poll_duration)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f'Error while consuming: {msg.error()}')
            else:
                # Parse the received message
                value = msg.value().decode('utf-8')
                lap = value.split()[2]
                dist = value.split()[4]
                race_completion = ((distance_per_lap*(float(lap)) + float(dist.rstrip("m")))/(distance_per_lap*total_lap)) * 100
                canvas.itemconfig(tagOrId=mercedes_lap_label, text=lap)
                canvas.itemconfig(tagOrId=mercedes_dist_label, text=dist)
                canvas.itemconfig(tagOrId=mercedes_percent_label, text="{:.0f}%".format(race_completion))


    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def redbull_time():
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe(["redbull_time"])

    try:
        while True:
            msg = consumer.poll(consumer_poll_duration)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f'Error while consuming: {msg.error()}')
            else:
                # Parse the received message
                value = msg.value().decode('utf-8')
                canvas.itemconfig(tagOrId=rb_time_label, text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()


def mercedes_time():
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe(["mercedes_time"])

    try:
        while True:
            msg = consumer.poll(consumer_poll_duration)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f'Error while consuming: {msg.error()}')
            else:
                # Parse the received message
                value = msg.value().decode('utf-8')
                canvas.itemconfig(tagOrId=mercedes_time_label, text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def redbull_pitstop():
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe(["redbull_pitstop"])

    try:
        while True:
            msg = consumer.poll(consumer_poll_duration)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f'Error while consuming: {msg.error()}')
            else:
                # Parse the received message
                value = msg.value().decode('utf-8')
                if len(value.split()) == 2:
                    fuel = value.split()[0]
                    tyre = value.split()[1]
                    value = "+" + str(fuel) + r"% fuel, +" + str(tyre) + r"% tyre health"
                if value == "pitstop_requested":
                    value = "Pitstop Requested"
                elif value == "at_pitstop":
                    value = "Service in Progress"

                canvas.itemconfig(tagOrId=rb_pitstop_label, text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def mercedes_pitstop():
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe(["mercedes_pitstop"])

    try:
        while True:
            msg = consumer.poll(consumer_poll_duration)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f'Error while consuming: {msg.error()}')
            else:
                # Parse the received message
                value = msg.value().decode('utf-8')
                if len(value.split()) == 2:
                    fuel = value.split()[0]
                    tyre = value.split()[1]
                    value = "+" + str(fuel) + r"% fuel, +" + str(tyre) + r"% tyre health"
                if value == "pitstop_requested":
                    value = "Pitstop Requested"
                elif value == "at_pitstop":
                    value = "Service in Progress"

                canvas.itemconfig(tagOrId=mercedes_pitstop_label, text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def redbull_fuel():
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe(["redbull_fuel"])

    try:
        while True:
            msg = consumer.poll(consumer_poll_duration)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f'Error while consuming: {msg.error()}')
            else:
                # Parse the received message
                value = msg.value().decode('utf-8').rstrip("%")
                rb_fuel_var.set(float(value))
                rb_fuel_progress["value"] = float(value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def mercedes_fuel():
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe(["mercedes_fuel"])

    try:
        while True:
            msg = consumer.poll(consumer_poll_duration)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f'Error while consuming: {msg.error()}')
            else:
                # Parse the received message
                value = msg.value().decode('utf-8').rstrip("%")
                mercedes_fuel_var.set(float(value))
                mercedes_fuel_progress["value"] = float(value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def redbull_tyre():
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe(["redbull_tyre"])

    try:
        while True:
            msg = consumer.poll(consumer_poll_duration)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f'Error while consuming: {msg.error()}')
            else:
                # Parse the received message
                value = msg.value().decode('utf-8').rstrip("%")
                rb_tyre_var.set(float(value))
                rb_tyre_progress["value"] = float(value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def mercedes_tyre():
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe(["mercedes_tyre"])

    try:
        while True:
            msg = consumer.poll(consumer_poll_duration)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f'Error while consuming: {msg.error()}')
            else:
                # Parse the received message
                value = msg.value().decode('utf-8').rstrip("%")
                mercedes_tyre_var.set(float(value))
                mercedes_tyre_progress["value"] = float(value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def redbull_speed():
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe(["redbull_speed"])

    try:
        while True:
            msg = consumer.poll(consumer_poll_duration)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f'Error while consuming: {msg.error()}')
            else:
                # Parse the received message
                value = msg.value().decode('utf-8')
                canvas.itemconfig(tagOrId=rb_speed_label, text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def mercedes_speed():
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe(["mercedes_speed"])

    try:
        while True:
            msg = consumer.poll(consumer_poll_duration)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f'Error while consuming: {msg.error()}')
            else:
                # Parse the received message
                value = msg.value().decode('utf-8')
                canvas.itemconfig(tagOrId=mercedes_speed_label, text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def redbull_crash():
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe(["redbull_crash"])

    try:
        while True:
            msg = consumer.poll(consumer_poll_duration)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f'Error while consuming: {msg.error()}')
            else:
                # Parse the received message
                value = msg.value().decode('utf-8')
                canvas.itemconfig(tagOrId=rb_crash_label, text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def mercedes_crash():
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe(["mercedes_crash"])

    try:
        while True:
            msg = consumer.poll(consumer_poll_duration)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f'Error while consuming: {msg.error()}')
            else:
                # Parse the received message
                value = msg.value().decode('utf-8')
                canvas.itemconfig(tagOrId=mercedes_crash_label, text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

# Threaded function to update the dashboard
def update_dashboard(consumer_func):
    while True:
        # Here you could add logic to retrieve and display stats for each consumer
        consumer_func()
        # label.config(text=f"{consumer_name}: {consumer_func()}")
        # sleep(2)

# Function to start a consumer thread
def start_consumer_thread(consumer_func):
    threading.Thread(target=update_dashboard, args=(consumer_func,), daemon=True).start()
    
##############################################################

# GUI stuff

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1920x960")
window.configure(bg = "#282828")


canvas = Canvas(
    window,
    bg = "#282828",
    height = 960,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    956.0,
    65.0,
    image=image_image_1
)

canvas.create_text(
    770.0,
    30.0,
    anchor="nw",
    text="Mercedes AMG Petronas",
    fill="#FFFFFF",
    font=("Helvetica", 32 * -1)
)

canvas.create_text(
    1288.0,
    30.0,
    anchor="nw",
    text="L. HAMILTON",
    fill="#FFFFFF",
    font=("Helvetica", 32 * -1)
)

mercedes_pitstop_label = canvas.create_text(
    960.0,
    145.0,
    anchor="center",
    text="NS",
    fill="#32D74B",
    font=("Helvetica", 32 * -1)
)

canvas.create_text(
    1432.0,
    136.0,
    anchor="nw",
    text="Tyre",
    fill="#FFFFFF",
    font=("Helvetica", 32 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    267.0,
    363.0,
    image=image_image_2
)

mercedes_speed_label = canvas.create_text(
    600.0,
    320.0,
    anchor="center",
    text="NS",
    fill="#01E6DE",
    font=("Helvetica", 134 * -1)
)

mercedes_percent_label = canvas.create_text(
    260.0,
    330.0,
    anchor="center",
    text="NS",
    fill="#FFFFFF",
    font=("Helvetica", 88 * -1)
)

mercedes_time_label = canvas.create_text(
    788.0,
    632.0,
    anchor="nw",
    text="NS",
    fill="#FFFFFF",
    font=("Helvetica", 50 * -1)
)

canvas.create_text(
    788.0,
    692.0,
    anchor="nw",
    text="Time",
    fill="#FFFFFF",
    font=("Helvetica", 36 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    158.0,
    683.0,
    image=image_image_3
)

mercedes_lap_label = canvas.create_text(
    244.0,
    626.0,
    anchor="nw",
    text="NS",
    fill="#FFFFFF",
    font=("Helvetica", 50 * -1)
)

canvas.create_text(
    244.0,
    686.0,
    anchor="nw",
    text="Lap",
    fill="#FFFFFF",
    font=("Helvetica", 36 * -1)
)

mercedes_dist_label = canvas.create_text(
    464.0,
    632.0,
    anchor="nw",
    text="NS",
    fill="#FFFFFF",
    font=("Helvetica", 50 * -1)
)

canvas.create_text(
    464.0,
    692.0,
    anchor="nw",
    text="Distance",
    fill="#FFFFFF",
    font=("Helvetica", 36 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    389.0,
    683.0,
    image=image_image_4
)

canvas.create_text(
    540.0,
    390.18841552734375,
    anchor="nw",
    text="Speed",
    fill="#01E6DE",
    font=("Helvetica", 46 * -1)
)

canvas.create_text(
    153.0,
    400.0,
    anchor="nw",
    text="Race Completion",
    fill="#FFFFFF",
    font=("Helvetica", 28 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    539.0,
    49.0,
    image=image_image_5
)

mercedes_fuel_var = DoubleVar()
mercedes_fuel_progress = ttk.Progressbar(orient="horizontal", length=200, variable=mercedes_fuel_var, maximum=100)
canvas.create_window(
    621.0, 155.0, anchor="center", window=mercedes_fuel_progress
)

mercedes_tyre_var = DoubleVar()
mercedes_tyre_progress = ttk.Progressbar(orient="horizontal", length=200, variable=mercedes_tyre_var, maximum=100)
canvas.create_window(
    1298.0, 155.0, anchor="center", window=mercedes_tyre_progress
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    461.0,
    155.0,
    image=image_image_8
)

rb_pitstop_label = canvas.create_text(
    960.0,
    790.0,
    anchor="center",
    text="NS",
    fill="#32D74B",
    font=("Helvetica", 32 * -1)
)

canvas.create_text(
    1432.0,
    782.0,
    anchor="nw",
    text="Tyre",
    fill="#FFFFFF",
    font=("Helvetica", 32 * -1)
)

rb_fuel_var = DoubleVar()
rb_fuel_progress = ttk.Progressbar(orient="horizontal", length=200, variable=rb_fuel_var, maximum=100)

canvas.create_window(
    621.0, 801.0, anchor="center", window=rb_fuel_progress
)

# rb_fuel_progress = canvas.create_text(
#     621.0, 801.0,
#     anchor="center",
#     text="NS",
#     fill="#FFFFFF",
#     font=("Helvetica", 50 * -1)
# )

rb_tyre_var = DoubleVar()
rb_tyre_progress = ttk.Progressbar(orient="horizontal", length=200, variable=rb_tyre_var, maximum=100)
canvas.create_window(
    1298.0, 801.0, anchor="center", window=rb_tyre_progress
)

# rb_tyre_progress = canvas.create_text(
#     1298.0, 801.0,
#     anchor="center",
#     text="NS",
#     fill="#FFFFFF",
#     font=("Helvetica", 50 * -1)
# )

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    461.0,
    801.0,
    image=image_image_11
)

mercedes_crash_label = canvas.create_text(
    577.0,
    497.0,
    anchor="nw",
    text="NS",
    fill="#FFFFFF",
    font=("Helvetica", 50 * -1)
)

canvas.create_text(
    577.0,
    557.0,
    anchor="nw",
    text="Crash Count",
    fill="#FFFFFF",
    font=("Helvetica", 36 * -1)
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    515.0,
    554.0,
    image=image_image_12
)

rb_crash_label = canvas.create_text(
    1304.0,
    501.0,
    anchor="nw",
    text="NS",
    fill="#FFFFFF",
    font=("Helvetica", 50 * -1)
)

canvas.create_text(
    1304.0,
    557.0,
    anchor="nw",
    text="Crash Count",
    fill="#FFFFFF",
    font=("Helvetica", 36 * -1)
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    1242.0,
    554.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    712.0,
    683.3740234375,
    image=image_image_14
)

rb_time_label = canvas.create_text(
    1734.0,
    624.0,
    anchor="nw",
    text="NS",
    fill="#FFFFFF",
    font=("Helvetica", 50 * -1)
)

canvas.create_text(
    1734.0,
    684.0,
    anchor="nw",
    text="Time",
    fill="#FFFFFF",
    font=("Helvetica", 36 * -1)
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    1104.0,
    675.0,
    image=image_image_15
)

rb_lap_label = canvas.create_text(
    1190.0,
    618.0,
    anchor="nw",
    text="NS",
    fill="#FFFFFF",
    font=("Helvetica", 50 * -1)
)

canvas.create_text(
    1190.0,
    678.0,
    anchor="nw",
    text="Lap",
    fill="#FFFFFF",
    font=("Helvetica", 36 * -1)
)

rb_dist_label = canvas.create_text(
    1410.0,
    624.0,
    anchor="nw",
    text="NS",
    fill="#FFFFFF",
    font=("Helvetica", 50 * -1)
)

canvas.create_text(
    1410.0,
    684.0,
    anchor="nw",
    text="Distance",
    fill="#FFFFFF",
    font=("Helvetica", 36 * -1)
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    1335.0,
    675.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    1658.0,
    675.3740234375,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=relative_to_assets("image_18.png"))
image_18 = canvas.create_image(
    1096.9999951043246,
    415.9999981641217,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=relative_to_assets("image_19.png"))
image_19 = canvas.create_image(
    962.0,
    894.0,
    image=image_image_19
)

canvas.create_text(
    849.0,
    875.0,
    anchor="nw",
    text="Red Bull Racing",
    fill="#FFFFFF",
    font=("Helvetica", 32 * -1)
)

canvas.create_text(
    1268.0,
    875.0,
    anchor="nw",
    text="M. VERSTAPPEN",
    fill="#FFFFFF",
    font=("Helvetica", 32 * -1)
)

image_image_20 = PhotoImage(
    file=relative_to_assets("image_20.png"))
image_20 = canvas.create_image(
    546.0,
    895.0,
    image=image_image_20
)

rb_speed_label = canvas.create_text(
    1330.0,
    320.0,
    anchor="center",
    text="NS",
    fill="#CC1E4A",
    font=("Helvetica", 134 * -1)
)

rb_percent_label = canvas.create_text(
    1675.0,
    330.0,
    anchor="center",
    text="NS",
    fill="#FFFFFF",
    font=("Helvetica", 88 * -1)
)

canvas.create_text(
    1265.0,
    390.1884765625,
    anchor="nw",
    text="Speed",
    fill="#CC1E4A",
    font=("Helvetica", 46 * -1)
)

canvas.create_text(
    1566.0,
    400.0,
    anchor="nw",
    text="Race Completion",
    fill="#FFFFFF",
    font=("Helvetica", 28 * -1)
)

image_image_21 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_21 = canvas.create_image(
    1680.0,
    363.0,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=relative_to_assets("image_22.png"))
image_22 = canvas.create_image(
    825.9999951043246,
    415.9999981641215,
    image=image_image_22
)

image_image_23 = PhotoImage(
    file=relative_to_assets("image_23.png"))
image_23 = canvas.create_image(
    823.0,
    369.0,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=relative_to_assets("image_24.png"))
image_24 = canvas.create_image(
    1097.0,
    369.0,
    image=image_image_24
)

canvas.create_rectangle(
    951.9999768766738,
    210.0,
    957.0,
    744.0,
    fill="#FFFFFF",
    outline="")

 # Start consumer threads
start_consumer_thread(redbull_distance)
start_consumer_thread(redbull_time)
start_consumer_thread(redbull_fuel)
start_consumer_thread(redbull_tyre)
start_consumer_thread(redbull_pitstop)
start_consumer_thread(redbull_speed)
start_consumer_thread(redbull_crash)

start_consumer_thread(mercedes_distance)
start_consumer_thread(mercedes_time)
start_consumer_thread(mercedes_fuel)
start_consumer_thread(mercedes_tyre)
start_consumer_thread(mercedes_pitstop)
start_consumer_thread(mercedes_speed)
start_consumer_thread(mercedes_crash)


window.resizable(False, False)
window.title(f"F1 Dashboard")
window.mainloop()
