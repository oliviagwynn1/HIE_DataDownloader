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

REQ_KEYS = [
    "_id",
    "session_data"
]

errormess = {
    0: {"message": "Missing key with ID"},
    1: {"message": "Missing key with session_data"},
    2: {"message": "Extra unknown key in data"}

}


def validate_keys(A):
    # check if session data exists
    if 'session_data' not in A.keys():
        raise KeyError
        logging.warning("Session_data key does not exist")
    # check type of session data
    else:
        if type(A["session_data"]) is not type({"hi":5,"hey":6}):
            print("nikki")
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
                            print(x)
                            logging.warning("Missing %s",x)
                            raise KeyError

    # check if id exists
    if '_id' not in A.keys():
        raise KeyError
    # check type of id data
    else:
        if type(A["_id"]) is not type("hey"):
            logging.warning("ID not a string")
            raise KeyError

    if len(A) is not 2:
        raise KeyError

    return 1

    # check type of session_data
    # id_t=type(newdict["_id"])
    # data_t=type(newdict["session_data"])

    # check type of _id
    # if id_t is not str:
    #     raise KeyError("ID given is not a string")
    # if data_t is not dict:
    #     raise KeyError("Session data given is not a dictionary")


@app.route("/api/luck/add_data", methods=["POST"])
def add_data():
    newdict = request.get_json()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["practice_Dec11"]
    mycol = mydb["Players"]

    # validate it has the right keys

    try:
        mycol.insert_one(newdict)
        print('added data to new key')
        kk = 'added data to new key'
    except DuplicateKeyError:
        print('key already exists ')

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
            print('added data to existing key')
            kk = 'added data to existing key'

    return jsonify(kk)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
