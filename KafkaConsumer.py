from confluent_kafka import Consumer
from confluent_kafka import KafkaError, KafkaException
import sys
import socket

conf = {'bootstrap.servers': '172.16.100.97:9092',
        'default.topic.config': {'api.version.request': True},
        'security.protocol': 'PLAINTEXT',
        'client.id': socket.gethostname(),
        'group.id': 'foo',
        'auto.offset.reset': 'smallest'}

consumer = Consumer(conf)

def consume_loop(topic):    
    # Subscribe to the Kafka topic
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(0.5)

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

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()