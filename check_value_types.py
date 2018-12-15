

def check_value_types(device_dict):
    """
    Checks value types on incoming POST dictionary

    Args:
        device_dict (dict): Incoming post request from
            front end

    Returns:
        TypeError (error): If the device dictionaries
            do not contain strings
    """
    players = device_dict['Players']
    mounts = device_dict['Mount_Points']

    if type(players) != list or type(mounts) != list:
        raise TypeError
