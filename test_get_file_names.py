from get_file_names import get_file_names
import os


def test_get_file_names():
    dir = os.getcwd() + '/Get_File_Name_Test_BIN'

    correct_out = []
    for i in range(10):
        path = dir + '/L' + str(i) + '.BIN'
        correct_out.append(path)

    assert sorted(get_file_names(dir)) == sorted(correct_out)
