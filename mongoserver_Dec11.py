import pymongo
from pymongo.errors import DuplicateKeyError
from flask import Flask, jsonify, request

from check_hash_server import check_hash_server
from search_db import searchdb
import logging

app = Flask(__name__)

# features to add:
# required keys
# make multiple requests for more than 1 player

logging.basicConfig(filename="Dec11_logging.txt",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

REQ_KEYS = [
    "_id",
    "session_data"
]

errormess = {
    0: {"message": "Structure of new data not correct"},
    1: {"message": "Data not received correctly"}

}


def validate_keys(A: object) -> object:
    # check if session data exists
    if 'session_data' not in A.keys():
        raise KeyError
        logging.warning("Session_data key does not exist")
    # check type of session data
    else:
        if not isinstance(A["session_data"], dict):
            raise TypeError
            logging.warning("Session_data is not a dictionary")
        # if it is a dict, check the keys in it
        else:
            reqkeys = ['hash', 'data', 'mod_time']
            # grab session data
            B = A["session_data"]
            # for each specific date
            for key in B:
                C = B[key]
                for key in C:
                    D = C[key]
                    for x in reqkeys:
                        if x not in D.keys():
                            logging.warning("Missing %s", x)
                            raise KeyError

    # check if id exists
    if '_id' not in A.keys():
        raise KeyError
    # check type of id data
    else:
        if not isinstance(A["_id"], str):
            logging.warning("ID not a string")
            raise KeyError

    if len(A) is not 2:
        raise KeyError


@app.route("/api/luck/add_data", methods=["POST"])
def add_data():
    newdict = request.get_json()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["practice_Dec11"]
    mycol = mydb["Players"]

    # validate it has the right keys
    try:
        validate_keys(newdict)
    except KeyError:
        logging.warning("Structure of data being added is wrong")
        return jsonify(errormess[0])
    except TypeError:
        logging.warning("Structure of data being added is wrong")
        return jsonify(errormess[0])

    # validate that data was received
    try:
        check_hash_server(newdict)
    except ValueError:
        logging.warning("Data not received correctly")
        return jsonify(errormess[1])

    # insert into database
    try:
        mycol.insert_one(newdict)
        hh = newdict["_id"]
        print('added data to new key')
        logging.info('added data to new player %s', hh)
    except DuplicateKeyError:
        logging.info('key already exists')

        # Grab new session dates
        session_dates = []
        session_data = newdict["session_data"]
        for keys, values in session_data.items():
            session_dates.append(keys)

        # Cycle through session_dates and add
        for date in session_dates:
            newkey = newdict["_id"]
            newdata = newdict["session_data"][date]
            myquery = {"_id": newkey}

            newvalues = {"$set": {"session_data." + date: newdata}}
            mycol.update_one(myquery, newvalues)
            print('added data to existing player', newkey)
            logging.info('added data to existing player %s', newkey)

    # check if added right afterwards
    # returns 1 if it does
    a = searchdb(newdict, mycol)

    return jsonify(a)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
