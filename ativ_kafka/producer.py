from time import sleep
from json import dumps
from kafka import KafkaProducer
import json
from uuid import uuid4

producer = KafkaProducer(bootstrap_servers=['54.152.185.215:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'),
                         key_serializer=lambda x: dumps(x).encode('utf-8'))

# for e in range(1):
data = {'nome' : 'Hugo', 'idade': '22', 'ip': '192.168.35.84'}
key = str(uuid4())
print(key)
producer.send('clientes', value=data, key=key, partition=3)
sleep(3)
