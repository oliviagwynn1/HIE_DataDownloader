

def check_be_list_length(device_dict):
    players = device_dict['Players']
    mounts = device_dict['Mount_Points']

    if len(players) != len(mounts):
        raise ValueError

    if not players or not mounts:
        raise ValueError
