

def get_serial_numbers(path):

    file = open(path, 'rb')
    header_block = file.readline(512)
    sn_bytes = header_block[416:420]
    sn = int.from_bytes(sn_bytes,  byteorder='little')

    return sn
