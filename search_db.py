import logging

logging.basicConfig(filename="Dec11_logging.txt",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


def searchdb(s_dict, mycol):
    """
    Confirms new data is in the db

    Args:
        s_dict: New diction of data
        mycol: Collection from database you are adding data to

    Returns:
        bool: True if database contains the new data

    Raises:
        KeyError: Key is missing and cannot access data

    """
    # myclient = pymongo.MongoClient(client)
    # mydb = myclient[db]
    # mycol = mydb[col]

    s_key = s_dict["_id"]
    myquery = {"_id": s_key}

    for key in s_dict['session_data']:
        A = s_dict["session_data"][key]
        datekey = key
        for key in A:
            filekey = key
            s_hash = A[key]["hash"]
            # CHECK IN DATABASE
            db_data = mycol.find(myquery)
            try:
                for x in db_data:
                    A = x["session_data"][datekey][filekey]["hash"]
                    if A == s_hash:
                        print("New data in db")
                        logging.info('Added data for user'
                                     ' %s, you can delete',
                                     s_key)
                        return True
                    else:
                        print("New data NOT in db")
                        logging.info("Didn't add data for %s,"
                                     " don't delete off device", s_key)
                        return False
            except:
                raise KeyError
