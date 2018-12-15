from base64 import b64decode, b64encode
import hashlib


def json_encode(bytes):
    """Saves hash (in bytes) as encoded JSON

    Args:
        bytes: hash from dictionary of data

    Returns:
        data_str (str): decoded hash from new data dict

    """
    data_bytes = b64encode(bytes)
    data_str = data_bytes.decode('utf-8')

    return data_str


def check_hash_server(newdict):
    """
    Confirms new hash matches hash sent in newdict

    Args:
        newdict: Dictionary of data from device to be uploaded


    """
    # Create list of time keys Sent:
    session_times = []
    session_data = newdict['session_data']
    for keys, values in session_data.items():
        session_times.append(keys)

    # Iterate through each session date sent
    for time in session_times:
        date_data = session_data[time]
        hashes = []
        newhashes = []

        # Iterate through the meta-dictionary
        for k, v in date_data.items():
            hasher = hashlib.md5()

            # Iterate through all sub-dictionaries
            if isinstance(v, dict):
                # Save sent hashes in list
                hashes.append(v['hash'])
                # Decode the data
                data_binary = b64decode(v['data'])
                # calculate hash of decoded data
                hasher.update(data_binary)
                # Digest Hash and save as JSON encoded form
                hash = hasher.digest()
                hash_str = json_encode(hash)
                # Add newly calculated hash to newhash list
                newhashes.append(hash_str)

        if hashes != newhashes:
            raise ValueError
