import threading
import tkinter as tk
from time import sleep

from confluent_kafka import Consumer
from confluent_kafka import KafkaError, KafkaException
import sys
import socket

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
                label.config(text=value)

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()



def kafka_consumer_3(label):
    label.config(text="redbull_distance")

def kafka_consumer_4(label):
    label.config(text="redbull_distance")


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

    # Labels for each consumer
    label_1 = tk.Label(root, text="Consumer 1: Not started", font=("Helvetica", 16))
    label_1.pack(pady=10)

    label_2 = tk.Label(root, text="Consumer 2: Not started", font=("Helvetica", 16))
    label_2.pack(pady=10)

    label_3 = tk.Label(root, text="Consumer 3: Not started", font=("Helvetica", 16))
    label_3.pack(pady=10)

    label_4 = tk.Label(root, text="Consumer 4: Not started", font=("Helvetica", 16))
    label_4.pack(pady=10)

    # Start consumer threads
    start_consumer_thread(redbull_distance, label_1)
    start_consumer_thread(mercedes_distance, label_2)
    # start_consumer_thread(kafka_consumer_3, label_3)
    # start_consumer_thread(kafka_consumer_4, label_4)

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    create_dashboard()
