import os


def get_file_names(dir):
    filenames = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".BIN"):
                filenames.append(file)

    return filenames
