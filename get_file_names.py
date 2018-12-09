import os

def get_file_names(dir):
    filenames = []
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in [f for f in filenames if f.endswith(".BIN")]:
            filenames.append(filename)

    return filenames