import tkinter as tk
from tkinter import messagebox
import time
from KafkaProducer import synchronous_produce_message
from tkinter import ttk
import threading
from confluent_kafka import Consumer, KafkaError
import socket

team = "redbull"
at_pitstop = False
current_fuel = 0
current_tyre = 0

conf = {'bootstrap.servers': '172.16.100.97:9092',
        'default.topic.config': {'api.version.request': True},
        'security.protocol': 'PLAINTEXT',
        'client.id': socket.gethostname(),
        'group.id': f"{team}_pitstop",
        'enable.auto.commit':'false',
        'auto.offset.reset': 'latest'}

def maintenance(fuel_units, tyre_units):
    global team
    key = 'maintenance'
    synchronous_produce_message(f"{team}_pitstop", key, f"{fuel_units} {tyre_units}")

def calculate_time():
    try:
        refuel_units = refuel_slider.get()
        tyre_units = tyre_slider.get()
        
        refuel_time = (refuel_units / 10) * 3  # 3 seconds per 10 units
        tyre_time = (tyre_units / 10) * 2  # 2 seconds per 10% tyre health
        
        total_time = refuel_time + tyre_time
        
        result_label.config(text=f"Estimated time: {total_time:.2f} seconds")
        
        return total_time
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integers for refuel units and tyre health.")
        return None

def start_maintenance():
    global at_pitstop
    if not at_pitstop:
        messagebox.showerror("Error", "Car is not at the pitstop!")
        return

    total_time = calculate_time()  # Ensure the time is calculated before starting
    if total_time is not None:
        refuel_units = refuel_slider.get()
        tyre_units = tyre_slider.get()

        # Start progress bar
        progress_bar['maximum'] = int(total_time * 100)  # Set max value for the progress bar
        progress_bar.start()
        
        # Simulate the maintenance process
        for i in range(int(total_time * 100)):
            time.sleep(0.01)  # Adjust the sleep time to control the speed of the progress bar
            progress_bar.step(1)
            root.update_idletasks()

        # Stop the progress bar
        progress_bar.stop()
        
        maintenance(refuel_units, tyre_units)
        
        at_pitstop = False
        messagebox.showinfo("Maintenance", "Maintenance complete!")

def consume_fuel_level():
    global team
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe([f"{team}_fuel"])

    try:
        while True:
            msg = consumer.poll(1)

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
                print(value)
                current_fuel = float(value[:-1])
                refuel_slider.config(to=100-current_fuel)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()


def consume_tyre_health():
    global team, current_tyre
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe([f"{team}_tyre"])

    try:
        while True:
            msg = consumer.poll(1)

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
                print(value, "tyre")
                current_tyre = float(value[:-1])
                tyre_slider.config(to=100-current_tyre)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def enable_controls():
    refuel_slider.config(state='normal', to=100-current_fuel)
    tyre_slider.config(state='normal', to=100-current_tyre)
    calculate_button.config(state='normal')
    start_button.config(state='normal')

def consume_pitstop_status():
    global at_pitstop, team
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe([f"{team}_pitstop"])

    try:
        while True:
            msg = consumer.poll(1)
            print(msg)

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
                print(value)
                if value == "at_pitstop":
                    at_pitstop = True
                    print("At pitstop")
                    # break

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

def start_consumer_pitstop_thread():
    consumer_thread = threading.Thread(target=consume_pitstop_status)
    consumer_thread.daemon = True  # Ensures the thread exits when the main program exits
    consumer_thread.start()

def start_consumer_fuel_thread():
    consumer_thread = threading.Thread(target=consume_fuel_level)
    consumer_thread.daemon = True  # Ensures the thread exits when the main program exits
    consumer_thread.start()

def start_consumer_tyre_thread():
    consumer_thread = threading.Thread(target=consume_tyre_health)
    consumer_thread.daemon = True  # Ensures the thread exits when the main program exits
    consumer_thread.start()

# Set up the GUI
root = tk.Tk()
root.title(f"F1 Pitstop Maintenance {team}")

tk.Label(root, text="Refuel Units:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
refuel_slider = tk.Scale(root, from_=0, to=100-current_fuel, orient='horizontal', state='normal')
refuel_slider.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Tyre Health %:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tyre_slider = tk.Scale(root, from_=0, to=100-current_tyre, orient='horizontal', state='normal')
tyre_slider.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate Time", command=calculate_time, state='normal')
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

start_button = tk.Button(root, text="Start Maintenance", command=start_maintenance, state='normal')
start_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Add a progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.grid(row=5, column=0, columnspan=2, pady=10)

# Start the Kafka consumer in separate threads
start_consumer_pitstop_thread()
start_consumer_fuel_thread()
start_consumer_tyre_thread()

root.mainloop()
