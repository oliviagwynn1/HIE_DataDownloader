from flask import Flask, jsonify, request
from pymodm import connect
from create_db import Player
import datetime
import logging

app = Flask(__name__)

# features to add:
# required keys
# make multiple requests for more than 1 player

logging.basicConfig(filename="luck_logging.txt",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


@app.route("/luck/add_data", methods=["POST"])
def add_data():
    connect("mongodb://nkm12:hello12345@ds123664.mlab.com:23664/concussion")
    a = request.get_json()

    try:
        p = Player.objects.raw({"_id": a["player_id"]}).first()
        player_id = Player.objects.raw({"_id": a["player_id"]})
        player_id.update({"$push": {"session_data": a["session_data"]}})
        result = {"message": "Successfully added data to existing player"}
        logging.info("New data added for existing player %s", a["player_id"])
    # if player does not exist, add them then add data
    except Player.DoesNotExist:
        player = Player(player_id=a["player_id"])
        player.save()
        # once add player, add data
        player_id = Player.objects.raw({"_id": a["player_id"]})
        player_id.update({"$push": {"session_data": a["session_data"]}})
        result = {"message": "Successfully added data to new player"}
        logging.info("Data added for new player %s", a["player_id"])

    now = datetime.datetime.now()
    player_id.update({"$push": {"time_stamp": now}})

    return jsonify(result)
