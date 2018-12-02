from flask import Flask, jsonify, request
from pymodm import connect
from create_db import Player
import datetime
import logging
app = Flask(__name__)

# features to add:
# required keys
# check if new player

logging.basicConfig(filename="luck_logging.txt",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

# create new player
@app.route("/luck/add_player", methods=["POST"])
def new_player():
    connect("mongodb://nkm12:hello12345@ds123664.mlab.com:23664/concussion")
    a = request.get_json()

    player = Player(player_id=a["player_id"])

    player.save()

    logging.info("New player added %s", a["player_id"])

    result = {"message": "Added new player"}

    return jsonify(result)


@app.route("/luck/add_data", methods=["POST"])
def add_data():

    connect("mongodb://nkm12:hello12345@ds123664.mlab.com:23664/concussion")
    a = request.get_json()

    #check if patient exists


    # add if new


    player_id = Player.objects.raw({"_id": a["player_id"]})
    #need to structure correctly
    player_id.update({"$push": {"data": a["data"]}})

    #add time when data when added
    now=datetime.datetime.now()
    player_id.update({"$push": {"time_stamp": now}})

    logging.info("New data added for player %s", a["player_id"])

    result = {"message": "Successfully added session data to DB"}


    return jsonify(result)
    # add data if already exists



#if __name__ == "__main__":
#    app.run(host="0.0.0.0")






