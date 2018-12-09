from flask import Flask, jsonify, request
from base64 import b64encode
import hashlib
app = Flask(__name__)


@app.route("/api/send_enc_file", methods=["GET"])
def send_enc_file():
    file = '/Users/clarkbulleit/Desktop/Class Folders/' \
           'Medical Software/Projects/bme590final/Test_BIN/L1.BIN'

    hasher = hashlib.md5()
    with open(file, 'rb') as afile:
        dat = afile.read()
        hasher.update(dat)

    hash = hasher.digest()
    hash_bytes = b64encode(hash)
    hash_str = hash_bytes.decode('utf-8')

    test_send = {
        'Hash': hash_str,
        'File': 2,
    }

    return jsonify(test_send)


if __name__ == "__main__":

    # First option is for development
    # Second option is for deployment
    app.run(host="127.0.0.1", port=5002)
    # app.run(host="0.0.0.0", port=5002)