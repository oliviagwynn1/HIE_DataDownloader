from base64 import b64encode


def encode_for_json(bytes):
    data_bytes = b64encode(bytes)
    data_str = data_bytes.decode('utf-8')

    return data_str