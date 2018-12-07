import os
import hashlib
from hashlib import md5, new


# function to check the path of where you are
def get_my_path():
    try:
        filename = __file__  # where we were when the module was loaded
    except NameError:  # fallback
        filename = inspect.getsourcefile(get_my_path)
    return os.path.realpath(filename)



def encode_then_hash_string(str):
    """
    encodes and then gives a hash
    :arg:   file or string you want to encode and hash
    :return: hash of file given
    """

    # make sure it is a string

    result = hashlib.md5(str.encode())

    return result


def bin_file(hi):
    # validate to make sure it is binary

    hasher = hashlib.md5()
    with open(hi, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)

    return hasher.digest()

def cmpHash(text1, text2):
    hash1 = hashlib.md5()
    hash1.update(text1)
    hash1 = hash1.hexdigest()

    hash2 = hashlib.md5()
    hash2.update(text2)
    hash2 = hash2.hexdigest()

    return  hash1 == hash2
