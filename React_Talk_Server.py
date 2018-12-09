from flask import Flask, jsonify, request
import hashlib
from get_file_names import get_file_names
from encode_for_json import encode_for_json
app = Flask(__name__)


@app.route("/api/send_enc_file", methods=["GET"])
def send_enc_file():
    dir = '/Users/clarkbulleit/Desktop/Class Folders/' \
           'Medical Software/Projects/bme590final/Test_BIN'

    filenames = get_file_names(dir)

    # read file and calculate hash
    hasher = hashlib.md5()
    with open(dir + '/' + filenames[2], 'rb') as afile:
        dat = afile.read()
        hasher.update(dat)
    hash = hasher.digest()

    # Encode hash and file for json serializing
    hash_str = encode_for_json(hash)
    dat_str = encode_for_json(dat)


    file_dict = {
        filenames[1]: hash_str,
        'XFile': dat_str,
    }

    return jsonify(file_dict)


if __name__ == "__main__":

    # First option is for development
    # Second option is for deployment
    app.run(host="127.0.0.1", port=5002)
    # app.run(host="0.0.0.0", port=5002)
