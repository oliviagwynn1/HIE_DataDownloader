import pymongo
from pymongo.errors import DuplicateKeyError
from flask import Flask, jsonify, request

from check_hash_server import check_hash_server
from search_db import searchdb
import logging

app = Flask(__name__)

logging.basicConfig(filename="database_server_log.txt",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

REQ_KEYS = [
    "_id",
    "session_data"
]

errormess = {
    0: {"message": "Structure of new data "
                   "not correct (missing key or extra key)"},
    1: {"message": "Data not received correctly, hashes don't match"},
    2: {"message": "Type of data for key is not correct"},
    3: {"message": "Data received correctly but not added to "
                   "database, do not delete off device"}

}


# check the structure is correct
def validate_keys(A: object) -> object:
    """
    Validates key, structure, and data in A

    Args:
        A: dictionary of new data sent to server

    Raises:
        KeyError: Key in dictionary does not match desired format of db
        TypeError: Type of data in key does not match desired format of db


    """
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
        logging.warning("Data is missing ID as a key")
        raise KeyError
    # check type of id data
    else:
        if not isinstance(A["_id"], str):
            logging.warning("ID not a string")
            raise TypeError

    if len(A) is not 2:
        logging.warning("Too many keys in the dictionary")
        raise KeyError


@app.route("/api/luck/add_data", methods=["POST"])
def add_data():
    """
    Adds data from dict to local DB from post request

    Returns:
        a (bool): If new data was correctly added
                to db and can be deleted (True = can delete)

    """
    newdict = request.get_json()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["practice_Dec11"]
    mycol = mydb["Players"]

    # validate it has the right keys
    try:
        validate_keys(newdict)
    except KeyError:
        logging.warning("Structure of data being added is wrong")
        ans = False
        return jsonify(ans)
    except TypeError:
        logging.warning("Structure of data being added is wrong")
        ans = False
        return jsonify(ans)

    # validate that data was received
    try:
        # Checksum of new hash and given hash
        check_hash_server(newdict)
        logging.info("Data received correctly")
    except ValueError:
        # Warning if hash not equal, data received in correct
        logging.warning("Data not received correctly")
        ans = False
        return jsonify(ans)

    # Insert into database
    try:
        # Add data to new player / ID
        mycol.insert_one(newdict)
        hh = newdict["_id"]
        print('added data to new key')
        logging.info('added data to new player %s', hh)
    except DuplicateKeyError:
        # Add data to existing player / ID
        logging.info("Attempting to add data to existing player")

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
            print('Added data to existing player', newkey)
            logging.info('Added data to existing player %s', newkey)

    # Check if data was added correctly to the database
    # Return True if added and it can be deleted
    try:
        a = searchdb(newdict, mycol)
        logging.info("Data added correctly to database, "
                     "you can delete off device")
    except KeyError:
        return jsonify(errormess[3])

    return jsonify(a)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
