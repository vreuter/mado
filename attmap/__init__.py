""" Package-scope definitions """

from ._att_map_like import AttMapLike
from .attmap import AttMap
from .attmap_echo import *
from .helpers import *
from .ordattmap import OrdAttMap
from .pathex_attmap import PathExAttMap
from ._version import __version__

AttributeDict = AttMap
AttributeDictEcho = AttMapEcho

__all__ = ["AttMapLike", "AttMap", "AttMapEcho", "AttributeDict",
           "AttributeDictEcho", "EchoAttMap", "OrdAttMap", "PathExAttMap",
           "get_data_lines"]
