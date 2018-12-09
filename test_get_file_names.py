from get_file_names import get_file_names


def test_get_file_names():
    dir = '/Users/clarkbulleit/Desktop/Class Folders/' \
          'Medical Software/Projects/bme590final/Test_BIN'

    correct_out = ['L0.BIN', 'L1.BIN', 'L2.BIN', 'L3.BIN',
                   'L4.BIN', 'L5.BIN', 'L6.BIN', 'L7.BIN',
                   'L8.BIN', 'L9.BIN']

    assert get_file_names(dir) == correct_out
