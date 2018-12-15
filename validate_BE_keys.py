

def validate_be_keys(keys, device_dict):
    """
    Validates that the keys for the dictionary are correct

     Args:
        keys (list): required keys as strings in list
        device_dict (dict): Incoming post request from
            front end

    Returns:
        KeyError (error): if the keys in the device_dict
            are not equal to the input keys
    """
    for key in keys:
        if key not in device_dict.keys() or \
                len(device_dict.keys()) != len(keys):
            raise KeyError
