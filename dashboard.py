import threading
import tkinter as tk
from time import sleep

from confluent_kafka import Consumer
from confluent_kafka import KafkaError, KafkaException
import sys
import socket

consumer_poll_duration = 1

conf = {'bootstrap.servers': '172.16.100.97:9092',
        'default.topic.config': {'api.version.request': True},
        'security.protocol': 'PLAINTEXT',
        'client.id': socket.gethostname(),
        'group.id': 'foo',
        'enable.auto.commit':'false',
        'auto.offset.reset': 'latest'}

# Boilerplate for Kafka consumer functions
def redbull_distance(label):
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
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()


def mercedes_distance(label):
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
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def redbull_time(label):
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
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()


def mercedes_time(label):
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
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def redbull_pitstop(label):
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
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def mercedes_pitstop(label):
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
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def redbull_fuel(label):
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
                value = msg.value().decode('utf-8')
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def mercedes_fuel(label):
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
                value = msg.value().decode('utf-8')
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def redbull_tyre(label):
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
                value = msg.value().decode('utf-8')
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def mercedes_tyre(label):
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
                value = msg.value().decode('utf-8')
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def redbull_speed(label):
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
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def mercedes_speed(label):
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
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def redbull_crash(label):
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
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def mercedes_crash(label):
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
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

# Threaded function to update the dashboard
def update_dashboard(label, consumer_func):
    while True:
        # Here you could add logic to retrieve and display stats for each consumer
        consumer_func(label)
        # label.config(text=f"{consumer_name}: {consumer_func()}")
        # sleep(2)

# Function to start a consumer thread
def start_consumer_thread(consumer_func, label):
    threading.Thread(target=update_dashboard, args=(label, consumer_func), daemon=True).start()

# Main dashboard GUI
def create_dashboard():
    root = tk.Tk()
    root.title("Kafka Consumers Dashboard")

    # Red Bull Labels
    rb_title_label = tk.Label(root, text="Red Bull", font=("Helvetica", 20, "bold"))
    rb_title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")

    tk.Label(root, text="Distance Covered:", font=("Helvetica", 16)).grid(row=1, column=0, sticky="w", padx=10)
    rb_dist_label = tk.Label(root, text="Not started", font=("Helvetica", 16))
    rb_dist_label.grid(row=1, column=1, sticky="w")

    tk.Label(root, text="Time Elapsed:", font=("Helvetica", 16)).grid(row=2, column=0, sticky="w", padx=10)
    rb_time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 16))
    rb_time_label.grid(row=2, column=1, sticky="w")

    tk.Label(root, text="Fuel Level:", font=("Helvetica", 16)).grid(row=3, column=0, sticky="w", padx=10)
    rb_fuel_label = tk.Label(root, text="Not started", font=("Helvetica", 16))
    rb_fuel_label.grid(row=3, column=1, sticky="w")

    tk.Label(root, text="Tyre Health:", font=("Helvetica", 16)).grid(row=4, column=0, sticky="w", padx=10)
    rb_tyre_label = tk.Label(root, text="Not started", font=("Helvetica", 16))
    rb_tyre_label.grid(row=4, column=1, sticky="w")

    tk.Label(root, text="Pitstop:", font=("Helvetica", 16)).grid(row=5, column=0, sticky="w", padx=10)
    rb_pitstop_label = tk.Label(root, text="Not started", font=("Helvetica", 16))
    rb_pitstop_label.grid(row=5, column=1, sticky="w")

    tk.Label(root, text="Speed:", font=("Helvetica", 16)).grid(row=6, column=0, sticky="w", padx=10)
    rb_speed_label = tk.Label(root, text="Not started", font=("Helvetica", 16))
    rb_speed_label.grid(row=6, column=1, sticky="w")

    tk.Label(root, text="Crash Count:", font=("Helvetica", 16)).grid(row=7, column=0, sticky="w", padx=10)
    rb_crash_label = tk.Label(root, text="0", font=("Helvetica", 16))
    rb_crash_label.grid(row=7, column=1, sticky="w")

    # Mercedes Labels
    mercedes_title_label = tk.Label(root, text="Mercedes", font=("Helvetica", 20, "bold"))
    mercedes_title_label.grid(row=8, column=0, columnspan=2, pady=20, sticky="w")

    tk.Label(root, text="Distance Covered:", font=("Helvetica", 16)).grid(row=9, column=0, sticky="w", padx=10)
    mercedes_dist_label = tk.Label(root, text="Not started", font=("Helvetica", 16))
    mercedes_dist_label.grid(row=9, column=1, sticky="w")

    tk.Label(root, text="Time Elapsed:", font=("Helvetica", 16)).grid(row=10, column=0, sticky="w", padx=10)
    mercedes_time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 16))
    mercedes_time_label.grid(row=10, column=1, sticky="w")

    tk.Label(root, text="Fuel Level:", font=("Helvetica", 16)).grid(row=11, column=0, sticky="w", padx=10)
    mercedes_fuel_label = tk.Label(root, text="Not started", font=("Helvetica", 16))
    mercedes_fuel_label.grid(row=11, column=1, sticky="w")

    tk.Label(root, text="Tyre Health:", font=("Helvetica", 16)).grid(row=12, column=0, sticky="w", padx=10)
    mercedes_tyre_label = tk.Label(root, text="Not started", font=("Helvetica", 16))
    mercedes_tyre_label.grid(row=12, column=1, sticky="w")

    tk.Label(root, text="Pitstop:", font=("Helvetica", 16)).grid(row=13, column=0, sticky="w", padx=10)
    mercedes_pitstop_label = tk.Label(root, text="Not started", font=("Helvetica", 16))
    mercedes_pitstop_label.grid(row=13, column=1, sticky="w")

    tk.Label(root, text="Speed:", font=("Helvetica", 16)).grid(row=14, column=0, sticky="w", padx=10)
    mercedes_speed_label = tk.Label(root, text="Not started", font=("Helvetica", 16))
    mercedes_speed_label.grid(row=14, column=1, sticky="w")

    tk.Label(root, text="Crash Count:", font=("Helvetica", 16)).grid(row=15, column=0, sticky="w", padx=10)
    mercedes_crash_label = tk.Label(root, text="0", font=("Helvetica", 16))
    mercedes_crash_label.grid(row=15, column=1, sticky="w")




    # Start consumer threads
    start_consumer_thread(redbull_distance, rb_dist_label)
    start_consumer_thread(redbull_time, rb_time_label)
    start_consumer_thread(redbull_fuel, rb_fuel_label)
    start_consumer_thread(redbull_tyre, rb_tyre_label)
    start_consumer_thread(redbull_pitstop, rb_pitstop_label)
    start_consumer_thread(redbull_speed, rb_speed_label)
    start_consumer_thread(redbull_crash, rb_crash_label)

    # start_consumer_thread(mercedes_distance, mercedes_dist_label)
    # start_consumer_thread(mercedes_time, rb_time_label)
    # start_consumer_thread(mercedes_fuel, mercedes_fuel_label)
    # start_consumer_thread(mercedes_tyre, mercedes_tyre_label)
    # start_consumer_thread(mercedes_pitstop, mercedes_pitstop_label)
    # start_consumer_thread(mercedes_speed, mercedes_speed_label)
    # start_consumer_thread(mercedes_crash, mercedes_crash_label)

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    create_dashboard()
