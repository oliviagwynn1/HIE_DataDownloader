import requests
import requests
from base64 import b64decode
from checksumdir import dirhash


if __name__ == "__main__":
    r = requests.get('http://127.0.0.1:5005/api/send_enc_file')
    raw_data = r.json()
    route = '/Users/clarkbulleit/Desktop/Test/'

    datadict = raw_data['Sessions']['date']

    for k, v in datadict.items():
        # decode data into binary
        data_binary = b64decode(v)
        # create new file with same name
        newfile = open(route + k, 'wb+')
        # Write binary data to file
        newfile.write(data_binary)

    # get hash calculated from original directory
    og_hash = raw_data['checksum']

    # Calculate new hash of new directory
    new_hash = dirhash(route, 'md5')

    # Print hashes and see if equal
    print(og_hash)
    print(new_hash)
    print(og_hash == new_hash)

