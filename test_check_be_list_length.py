import pytest
from check_be_list_length import check_be_list_length


@pytest.mark.parametrize("dev_dict", [
    ({'Mount_Points': [1, 2], 'Players': [1]}),
    ({'Mount_Points': ['s', 'p'], 'Players': [1]}),
    ({'Mount_Points': [], 'Players': []}),
])
def test_validate_be_keys(dev_dict):

    with pytest.raises(ValueError):
        check_be_list_length(dev_dict)
