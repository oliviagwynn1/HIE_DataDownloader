import pytest
from check_value_types import check_value_types


@pytest.mark.parametrize("dev_dict", [
    ({'Mount_Points': 1, 'Players': [1]}),
    ({'Mount_Points': 'str', 'Players': [1]}),
])
def test_validate_be_keys(dev_dict):

    with pytest.raises(TypeError):
        check_value_types(dev_dict)
