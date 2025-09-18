from kafka import KafkaProducer
import json, time

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    data = {"event": "click", "timestamp": time.time()}
    producer.send('events', value=data)
    time.sleep(1)
