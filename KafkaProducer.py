from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': '172.16.100.97:9092',
        'default.topic.config': {'api.version.request': True},
        'security.protocol': 'PLAINTEXT',
        'client.id': socket.gethostname()}

producer = Producer(conf)

def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

def produce_message(topic, key, value):
    producer.produce(topic, key=key, value=value, callback=acked)
    producer.flush()
