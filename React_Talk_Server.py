from flask import Flask, jsonify, request
import os
app = Flask(__name__)


@app.route("/api/send_enc_file", methods=["GET"])
def send_enc_file():
    file = '/Test_BIN/L0.BIN'
    enc = file.encode()

    test_send = {
        'Hash': 1,
        'File': 2,
    }

    return jsonify(test_send)


if __name__ == "__main__":

    # First option is for development
    # Second option is for deployment
    app.run(host="127.0.0.1", port=5002)
    # app.run(host="0.0.0.0", port=5002)
