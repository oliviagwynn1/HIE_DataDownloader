import os
import hashlib
from datetime import datetime
from checksumdir import dirhash
from get_file_names import get_file_names
from encode_for_json import encode_for_json


if __name__ == "__main__":
    dir = '/Volumes/MV1'

    # Calculate checksum of directory
    md5hash = dirhash(dir, 'md5')

    # Harvest Filenames from directory
    filenames = get_file_names(dir)

    # Setup output dictionary, include checksum
    output_dictionary = {
        'checksum': md5hash,
    }

    # output_dictionary = {}
    # read files, encode, calculate hash, and put in dictionary
    for name in filenames:
        hasher = hashlib.md5()
        with open(name, 'rb') as afile:
            dat = afile.read()
            hasher.update(dat)

        hash = hasher.digest()
        # Encode hash and file for json serializing
        dat_str = encode_for_json(dat)
        hash_str = encode_for_json(hash)

        # Get modification and creation timestamp and convert to datetime
        tm_stamp = os.path.getmtime(name)
        mod_time = datetime.fromtimestamp(tm_stamp).strftime('%Y-%m-%d %H:%M:%S')

        # create nested dictionary for each file and add to bit dict
        file_dict = {
            'data': dat_str,
            'modification_time': mod_time,
            'hash': hash_str,
        }
        output_dictionary[os.path.basename(name)] = file_dict