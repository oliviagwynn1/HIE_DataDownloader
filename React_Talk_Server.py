from flask import Flask, jsonify, request
import os
from datetime import datetime
from checksumdir import dirhash
from get_file_names import get_file_names
from encode_for_json import encode_for_json
app = Flask(__name__)


@app.route("/api/send_enc_file", methods=["GET"])
def send_enc_file():
    dir = '/Users/clarkbulleit/Desktop/Class Folders/' \
           'Medical Software/Projects/bme590final/Test_BIN'

    # Calculate checksum of directory
    md5hash = dirhash(dir, 'md5')

    # Harvest Filenames from directory
    filenames = get_file_names(dir)

    # Setup output dictionary, include checksum
    output_dictionary = {
        'checksum': md5hash,
    }

    # read files, encode, and put in dictionary
    for name in filenames:
        with open(dir + '/' + name, 'rb') as afile:
            dat = afile.read()

        # Encode hash and file for json serializing
        dat_str = encode_for_json(dat)

        # Get modification and creation timestamp and convert to datetime
        tm_stamp = os.path.getmtime(dir + '/' + name)
        mod_time = datetime.fromtimestamp(tm_stamp).strftime('%Y-%m-%d %H:%M:%S')

        # create nested dictionary for each file and add to bit dict
        file_dict = {
            'data': dat_str,
            'modification_time': mod_time,
        }
        output_dictionary[name] = file_dict

    return jsonify(output_dictionary)


if __name__ == "__main__":

    # First option is for development
    # Second option is for deployment
    app.run(host="127.0.0.1", port=5002)
    # app.run(host="0.0.0.0", port=5002)
