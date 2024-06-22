from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.serializer import kafka_decode, kafka_encode

from core.conf.environ import env


ports = [env('KAFKA_PORT1'), env('KAFKA_PORT2'), env('KAFKA_PORT3')]
KAFKA_BROKER_URL = [f'localhost:{ports[0]}', f'localhost:{ports[1]}', f'localhost:{ports[2]}']
KAFKA_TOPIC = 'chat-topic'


def get_kafka_producer():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=kafka_encode
    )
    return producer
# переписать в класс && добавить проверку на существование топика && добавить проверку на существование брокера && добавить возможность писать топик/группу && добавить хендлеры ошибок


def get_kafka_consumer():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        boostrap_servers=KAFKA_BROKER_URL,
        auto_offset_reset='earliest',
        groupd_id='example-group',
        value_deserializer=kafka_decode
    )
    return consumer


def create_kafka_topic(topic_name, partitions, replication_factor):
    admin_client = KafkaAdminClient(bootstrap_servers=KAFKA_BROKER_URL, client_id='example-client')
    topic_list = [NewTopic(topic_name, partitions, replication_factor)]
    admin_client.create_topics(new_topics=topic_list, validate_only=False)
