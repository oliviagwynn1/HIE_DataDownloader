from flask import Flask, request
app = Flask(__name__)


@app.route("/api/new_patient", methods=["POST"])
def send_enc_file():

    return


if __name__ == "__main__":

    # First option is for development
    # Second option is for deployment
    # app.run(host="127.0.0.1", port=5002)
    app.run(host="0.0.0.0", port=5002)