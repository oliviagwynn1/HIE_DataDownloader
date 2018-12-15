import pytest
from mongoserver_Dec11 import validate_keys


@pytest.mark.parametrize("newdict,expected", [
    # correct keys
    ({'_id': '5',
      'session_data': {'date': {'LBIN': {'data': 'jalkaf',
                                         'hash': 'akld',
                                         'mod_time': 'datetime'
                                         }
                                }
                       }
      },
     1),
    ({'_id': '5',
      'session_data': {'date': {'LBIN': {'data': 'danf',
                                         'hash': 'dfjal',
                                         'mod_time': 'datetime'}},
                       'date2': {'LBIN': {'data': 'danf',
                                          'hash': 'dfjal',
                                          'mod_time': 'datetime'}}
                       }}, 1)

])
def test_validate_parametrize(newdict, expected):
    assert validate_keys(newdict) is None


def test_validate_no_session():
    newdict = {"_id": "567"}
    with pytest.raises(KeyError):
        validate_keys(newdict)


def test_validate_no_id():
    newdict = {'session_data': {'date': dict(LBIN=dict(data='danf',
                                                       hash='dfjal',
                                                       mod_time='datetime')),
                                'date2': dict(LBIN=dict(data='danf',
                                                        hash='dfjal',
                                                        mod_time='datetime'))}}
    with pytest.raises(KeyError):
        validate_keys(newdict)


def test_extra_id():
    newdict = \
        {'_id': '5',
         'session_data':
             {'date': {'LBIN': {'data': 'dnf',
                                'hash': 'dfjal',
                                'mod_time': 'datetime'}},
              'date2': {'LBIN': {'data': 'danf',
                                 'hash': 'dfjal',
                                 'mod_time': 'datetime'}}},
         'extra_id': "6"}

    with pytest.raises(KeyError):
        validate_keys(newdict)


def test_sess_not_dict():
    newdict = {'_id': "6",
               'session_data':
                   12}
    with pytest.raises(TypeError):
        validate_keys(newdict)


def test_sess_not_dict2():
    newdict = {'_id': "6",
               'session_data':
                   12}
    with pytest.raises(TypeError):
        validate_keys(newdict)
