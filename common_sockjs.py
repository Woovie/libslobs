import json

def decode_sockjs_array(arr: str):
    return json.loads(json.loads(arr[2:-1]))

def encode_sockjs_array(arr: dict):
    return json.dumps(json.dumps(arr))