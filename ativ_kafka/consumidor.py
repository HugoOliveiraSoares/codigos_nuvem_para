from kafka import KafkaConsumer
from datetime import datetime


topic_name = 'clientes'

consumer = KafkaConsumer(topic_name, bootstrap_servers=['54.152.185.215:9092'], group_id=None, 
auto_offset_reset='smallest', consumer_timeout_ms = 5000)

print('Consumindo mensagens do tópico: ')
for message in consumer:
    if message is not None:
        print('Topico....: ' + str(message.topic))
        print('Particao..: ' + str(message.partition))
        print('Offset....: ' + str(message.offset))
        print('Timestamp.: ' + str(message.timestamp))
        print('Data/Hora.: ' + str(datetime.fromtimestamp(message.timestamp / 1000.0)))
        print('Chave.....: ' + str(message.key))
        print('Valor.....: ' + message.value.decode('utf-8'))
        print('')


consumer.close()
print('Fim')

