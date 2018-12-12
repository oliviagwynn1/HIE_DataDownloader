from flask import Flask, jsonify, request
import os
import hashlib
from flask_cors import CORS
from datetime import datetime
from checksumdir import dirhash
from get_file_names import get_file_names
from encode_for_json import encode_for_json
app = Flask(__name__)
CORS(app)


@app.route("/api/send_enc_file", methods=["GET"])
def send_enc_file():
    dir = '/Users/clarkbulleit/Desktop/Class Folders/' \
           'Medical Software/Projects/bme590final/Test_BIN'

    # dir = '/Volumes/MV1'

    # Calculate checksum of directory
    # md5hash = dirhash(dir, 'md5')

    # Harvest Filenames from directory
    filenames = get_file_names(dir)

    # Pull all of the filenames and get a list of dates
    session_dates = set()
    for file in filenames:
        date_stamp = os.path.getmtime(file)
        session_date = datetime.fromtimestamp(date_stamp).strftime('%Y-%m-%d')
        session_dates.add(session_date)

    # Setup output dictionary
    output_dictionary = {
        '_id': '2',
        'session_data': {},
    }

    # Input a session date for each of the session dates pulled
    for date in session_dates:
        output_dictionary['session_data'][date] = {}

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
        mod_date = datetime.fromtimestamp(tm_stamp).strftime('%Y-%m-%d')

        # create nested dictionary for each file and add to bit dict
        file_dict = {
            'data': dat_str[0:10],
            'mod_time': mod_time,
            'hash': hash_str,
        }
        output_dictionary['session_data'][mod_date][os.path.basename(name).replace(".BIN", "")] = file_dict

    return jsonify(output_dictionary)


if __name__ == "__main__":

    # First option is for development
    # Second option is for deployment
    app.run(host="127.0.0.1", port=5005)
    # app.run(host="0.0.0.0", port=5002)
