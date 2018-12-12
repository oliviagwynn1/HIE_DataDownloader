import pymongo
from pymongo.errors import DuplicateKeyError
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# features to add:
# required keys
# make multiple requests for more than 1 player

logging.basicConfig(filename="Dec11_logging.txt",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

@app.route("/api/luck/add_data", methods=["GET"])
def add_data():

    newdict = request.get_json()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["practice_Dec11"]
    mycol = mydb["Players"]

    #validate it has the right keys

    newkey = newdict["_id"]
    newdata = newdict["session_data"]
    myquery = {"_id": newkey}

    try:
        x = mycol.insert_one(newdict)
        print('added data to new key')
        kk='added data to new key'
    except DuplicateKeyError:
        print('key already exists ')
        #possibly change if don't need
        matchingdata = mycol.find(myquery)
        for x in matchingdata:
            newvalues = {"$set": newdata}
            mycol.update_one(myquery, newvalues)
            print('added data to existing key')
            kk='added data to existing key'

    return jsonify(kk)


if __name__ == "__main__":
    app.run(host="0.0.0.0")













