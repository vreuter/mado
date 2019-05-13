""" Tests for the echo behavior """

import pytest
from attmap import AttMap, AttMapEcho
from veracitools import ExpectContext

__author__ = "Vince Reuter"
__email__ = "vreuter@virginia.edu"


def exec_get_item(m, k):
    """
    Request value for given key in a mapping.

    :param Mapping m: mapping on which to query key
    :param str k: key for which to request value
    :return object: result of requesting key's value from the map
    """
    return m[k]


@pytest.mark.parametrize(
    ["maptype", "getter", "key", "expected"],
    [(AttMap, getattr, "missing_key", AttributeError),
     (AttMap, exec_get_item, "random", KeyError),
     (AttMapEcho, exec_get_item, "arbkey", KeyError),
     (AttMapEcho, getattr, "missing_key", "missing_key")])
def test_echo_is_type_dependent_and_access_dependent(
        maptype, getter, key, expected):
    """ Retrieval of missing key/attr echoes it iff the type and access mode permit. """
    m = maptype()
    assert key not in m
    with ExpectContext(expected, getter) as ctx:
        ctx(m, key)
