

def check_be_list_length(device_dict):
    """
    Ensure that Player ids and mount lengths are
    equal

    Args:
        device_dict (dict): Incoming post request from
            front end

    Returns:
        ValueError (error): if the mount list and the
            player list are not the same length
    """
    players = device_dict['Players']
    mounts = device_dict['Mount_Points']

    if len(players) != len(mounts):
        raise ValueError

    if not players or not mounts:
        raise ValueError
