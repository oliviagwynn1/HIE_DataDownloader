import os


def get_file_names(dir):
    filenames = []
    for root, dirs, files in os.walk(dir):
        path = root.split(os.sep)
        for file in files:
            if file.endswith(".BIN"):
                filenames.append(os.path.join(root, file))

    return filenames
