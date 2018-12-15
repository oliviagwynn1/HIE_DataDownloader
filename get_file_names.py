import os


def get_file_names(dir):
    """
    Gets all .BIN filenames from a given directory

    Args:
        dir (dict): Route to directory

    Returns:
        filenames (list): List of full routes
            to all .BIN files within the given
            directory
    """
    filenames = []
    for root, dirs, files in os.walk(dir):
        path = root.split(os.sep)
        for file in files:
            if file.endswith(".BIN"):
                filenames.append(os.path.join(root, file))

    return filenames
