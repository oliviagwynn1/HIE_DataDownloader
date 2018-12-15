from encode_for_json import encode_for_json


def test_encode_for_json():
    bin = b'\x14B\xcc8\x0ep\xb7\xb6_\xd3\xe0\xf8nz\xa2\xf1'
    correct_out = 'FELMOA5wt7Zf0+D4bnqi8Q=='

    assert encode_for_json(bin) == correct_out
