import json

def kafka_encode(data):
    return json.dumps(data).encode('utf-8')

def kafka_decode(data):
    return json.loads(data.decode('utf-8'))