from flask import Flask, jsonify, request
import os
import hashlib
from flask_cors import CORS
from datetime import datetime
from checksumdir import dirhash
import requests
from get_file_names import get_file_names
from validate_BE_keys import validate_be_keys
from encode_for_json import encode_for_json
from get_serial_numbers import get_serial_numbers
from check_value_types import check_value_types
from check_be_list_length import check_be_list_length
import logging
app = Flask(__name__)
CORS(app)

error_messages = {
        0: {"message": "Post Keys not correct"},
        1: {"message": "Device dictionary keys are not lists"},
        2: {"message": "Device dictionary lists are not equal"},
        3: {"message": "Cannot connect to remote server"},
        }

logging.basicConfig(filename="Main_Log.txt",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


@app.route("/api/send_data", methods=["POST"])
def send_data():
    """
    Receives dictionary with the form
    device_data = {
        'Players': ['261758686', '261813717'],
        'Mount_Points': ['/Volumes/MV1', '/Volumes/MV1 1'],
        'Num_Files': [609, 14],
    }
    That contains the serial number and the matched location
    :return:
    """

    # Set up responses dictionary
    responses = {}

    # Pull data from Post request
    device_dict = request.get_json()

    # validate keys in dictionary
    keys = ['Mount_Points', 'Num_Files', 'Players']
    try:
        validate_be_keys(keys, device_dict)
    except KeyError:
        logging.warning(error_messages[0])
        return jsonify(error_messages[0]), 500

    # Make sure data is in correct form
    try:
        check_value_types(device_dict)
    except TypeError:
        logging.warning(error_messages[1])
        return jsonify(error_messages[1]), 500

    # Make sure the lists have equal length, not empty
    try:
        check_be_list_length(device_dict)
    except ValueError:
        logging.warning(error_messages[2])
        return jsonify(error_messages[2]), 500

    # Get device information dictionary and pull route to device
    # dir is route to the device, the value in the dict
    # SN is the serial number, the key in the dictionary
    for i, player in enumerate(device_dict['Players']):
        dir = device_dict['Mount_Points'][i]
        SN = player

        # Harvest Filenames from directory
        filenames = get_file_names(dir)

        # Pull all of the filenames and get a list of dates
        session_dates = set()
        for file in filenames:
            date_stamp = os.path.getmtime(file)
            session_date = datetime.fromtimestamp(date_stamp)\
                .strftime('%Y-%m-%d')
            session_dates.add(session_date)

        # Setup output dictionary
        output_dictionary = {
            '_id': SN,
            'session_data': {},
        }

        # Input a session date for each of the session dates pulled
        for date in session_dates:
            output_dictionary['session_data'][date] = {}

        # read files, encode, calculate hash, and put in dictionary
        for name in filenames:
            hasher = hashlib.md5()
            with open(name, 'rb') as afile:
                dat = afile.read()
                hasher.update(dat)

            hash = hasher.digest()

            # Encode hash and file for json serializing
            dat_str = encode_for_json(dat)
            hash_str = encode_for_json(hash)

            # Get modification and creation timestamp and convert to datetime
            tm_stamp = os.path.getmtime(name)
            mod_time = datetime.fromtimestamp(tm_stamp).\
                strftime('%Y-%m-%d %H:%M:%S')
            mod_date = datetime.fromtimestamp(tm_stamp).\
                strftime('%Y-%m-%d')

            # create nested dictionary for each file and add to bit dict
            file_dict = {
                'data': dat_str[0:10],
                'mod_time': mod_time,
                'hash': hash_str,
            }
            output_dictionary['session_data'][mod_date][
                os.path.basename(name).replace(
                    ".BIN", "")] = file_dict
        # Post a dictionary for each Serial number to the server
        try:
            r = requests.post(
                'http://vcm-7335.vm.duke.edu:5010/api/luck/add_data',
                json=output_dictionary)
        except requests.exceptions.ConnectionError:
            logging.warning(error_messages[3])
            return jsonify(error_messages[3]), 500

        # Turn responses into a dictionary
        responses[SN] = r.json()

    return jsonify(responses)


@app.route("/api/send_device_info", methods=["GET"])
def send_device_info():

    # Set path to /Volumes for mac, will be different for PC
    dir = '/Volumes/'
    # dir = '/Users/clarkbulleit/Desktop/Test/'

    # Setup up device_data output dictionary
    device_data = {
        'Players': [],
        'Mount_Points': [],
        'Num_Files': [],
    }

    # Only get directory names in the first layer
    volumes = []
    for root, dirs, files in os.walk(dir):
        volumes.extend(dirs)
        break

    # Cycle through devices mounted in Volumes
    for volume in volumes:
        if volume != 'Macintosh HD':
            path = dir + volume
            filenames = get_file_names(path)
            num_files = len(filenames)
            sn = get_serial_numbers(filenames[-1])

            # Put information into dictionary
            device_data['Players'].append(sn)
            device_data['Mount_Points'].append(path)
            device_data['Num_Files'].append(num_files)

    return jsonify(device_data)


if __name__ == "__main__":

    # First option is for development
    # Second option is for deployment
    app.run(host="127.0.0.1", port=5005)
    # app.run(host="0.0.0.0", port=5002)
