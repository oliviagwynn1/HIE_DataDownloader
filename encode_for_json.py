from base64 import b64encode


def encode_for_json(bytes):
    """
    Encoded bytes into JSON serializable string

    Args:
        bytes (bytearray): bytes to put in JSOn

    Returns:
        data_str (str): encoded bytes in utf-8 format
            for JSON serialization
    """
    data_bytes = b64encode(bytes)
    data_str = data_bytes.decode('utf-8')

    return data_str
