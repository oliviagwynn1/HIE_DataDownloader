

def check_value_types(device_dict):
    players = device_dict['Players']
    mounts = device_dict['Mount_Points']

    if type(players) != list or type(mounts) != list:
        raise TypeError
