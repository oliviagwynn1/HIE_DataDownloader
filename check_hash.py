import requests
from base64 import b64decode
import hashlib
from encode_for_json import encode_for_json


if __name__ == "__main__":
    # r = requests.get('http://127.0.0.1:5005/api/send_enc_file')
    r = requests.get('http://vcm-7335.vm.duke.edu:5004/api/send_enc_file')
    data = r.json()

    # Sets up one list for the harvested hashes, another for the calculated ones
    hashes = []
    newhashes = []

    # Iterate through the meta-dictionary
    for k, v in data.items():
        hasher = hashlib.md5()

        # Iterate through all sub-dictionaries
        if isinstance(v, dict):

            # Save sent hashes in list
            hashes.append(v['hash'])
            # Decode the data
            data_binary = b64decode(v['data'])
            # Write to local file
            # calculate hash of decoded data
            hasher.update(data_binary)
            # Digest Hash and save as JSON encoded form
            hash = hasher.digest()
            hash_str = encode_for_json(hash)
            # Add newly calculated hash to newhash list
            newhashes.append(hash_str)

    print(type(hashes[0]))
    print(newhashes)
    print(hashes == newhashes)

