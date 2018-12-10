from get_file_names import get_file_names


def test_get_file_names():
    dir = '/Users/clarkbulleit/Desktop/Class Folders/' \
          'Medical Software/Projects/bme590final/Get_File_Name_Test_BIN'

    correct_out = []
    for i in range(10):
        path = dir + '/L' + str(i) + '.BIN'
        correct_out.append(path)

    assert get_file_names(dir) == correct_out
