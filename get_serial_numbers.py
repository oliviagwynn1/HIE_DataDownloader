

def get_serial_numbers(path):
    """
        Reads the serial number from .BIN file

        Args:
            path (str): route to file

        Returns:
            sn (int): the serial number found in
                the header of the file
     """
    file = open(path, 'rb')
    header_block = file.read()
    sn_bytes = header_block[416:420]
    sn = int.from_bytes(sn_bytes,  byteorder='little')

    return sn
