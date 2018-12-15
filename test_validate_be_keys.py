import pytest
from validate_BE_keys import validate_be_keys


@pytest.mark.parametrize("keys, dict", [
    (['Mount_Points', 'Num_Files', 'Players'],
     {'Num_Files': [1], 'Players': [1]}),
    (['Mount_Points', 'Num_Files', 'Players'],
     {'Num_Files': [1], 'Players': [1],
      'Num_Files': [1], 'Players': [1]}),
])
def test_validate_be_keys(keys, dict):

    with pytest.raises(KeyError):
        validate_be_keys(keys, dict)
