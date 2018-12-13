

def validate_be_keys(keys, device_dict):
    for key in keys:
        if key not in device_dict.keys() or \
                len(device_dict.keys()) != len(keys):
            raise KeyError
