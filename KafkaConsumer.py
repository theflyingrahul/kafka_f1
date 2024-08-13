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


def consume_loop(topic):
    consumer = Consumer(conf)

    # Subscribe to the Kafka topic
    consumer.subscribe([topic])

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
                return value

    except KeyboardInterrupt:
        pass
    finally:
        # Close the consumer gracefully
        consumer.close()

print(consume_loop("redbull_distance"))