import os


def get_file_names(dir):
    filenames = []
    for dirpath, dirnames, filenames in os.walk(dir):
        for filename in [f for f in filenames if f.endswith(".BIN")]:
            filenames.append(filename)

    times = []
    for name in filenames:
        times.append(os.path.getmtime(dir + '/' + name))

    file_info = {
        'filenames': filenames,
        'mod_times': times,
    }
    return file_info
