import requests
from base64 import b64decode
import hashlib
from encode_for_json import encode_for_json


if __name__ == "__main__":
    r = requests.post('http://127.0.0.1:5005/api/send_enc_file',
                      json=device_data)
    # r = requests.get('http://vcm-7335.vm.duke.edu:5004/api/send_enc_file')
    data = r.json()

    # Create list of time keys Sent:
    session_times = []
    session_data = data['Sessions']
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
                hash_str = encode_for_json(hash)
                # Add newly calculated hash to newhash list
                newhashes.append(hash_str)

        if hashes != newhashes:
            raise ValueError
            print('All data for session date {0} was received properly'
                  .format(time))
        else:
            print('Data on {0} was not received properly'.format(time))

    # print(hashes)
    # print(newhashes)
    # print(hashes == newhashes)
