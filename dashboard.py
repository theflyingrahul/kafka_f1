import threading
import tkinter as tk
from time import sleep

from KafkaConsumer import consume_loop

# Boilerplate for Kafka consumer functions
def redbull_distance(label):
    # print(consume_loop("redbull_distance"))
    text = consume_loop("redbull_distance")
    print(text)
    label.config(text=text)


def mercedes_distance(label):
    label.config(text=consume_loop("mercedes_distance"))

def kafka_consumer_3(label):
    label.config(text=consume_loop("redbull_distance"))


def kafka_consumer_4(label):
    label.config(text=consume_loop("redbull_distance"))


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
    # start_consumer_thread(mercedes_distance, label_2)
    # start_consumer_thread(kafka_consumer_3, label_3)
    # start_consumer_thread(kafka_consumer_4, label_4)

    # Start the GUI loop
    root.mainloop()

if __name__ == "__main__":
    create_dashboard()
