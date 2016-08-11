"""Common constants."""

from enum import Enum
import re
from .typealiases import YangIdentifier

class YangsonException(Exception):
    """Base class for all Yangson exceptions."""
    pass

class NonexistentSchemaNode(YangsonException):
    """Exception to be raised when a schema node doesn't exist."""

    def __init__(self, name: YangIdentifier,
                 ns: YangIdentifier = None) -> None:
        self.name = name
        self.ns = ns

    def __str__(self) -> str:
        return "{} in module {}".format(self.name, self.ns)

# Regular expressions

_ident = "[a-zA-Z_][a-zA-Z0-9_.-]*"
ident_re = re.compile(_ident)
_pname = "((?P<prf>{}):)?(?P<loc>{})".format(_ident, _ident)
pname_re = re.compile(_pname)
_rhs = """("(?P<drhs>[^"]*)"|'(?P<srhs>[^']*)')"""
pred_re = re.compile(
    r"\[\s*(({}|\.)\s*=\s*{}|(?P<pos>\d*))\s*\]".format(_pname, _rhs))
ws_re = re.compile(r"[ \n\t\r]*")
_integer = "[0-9]+"
integer_re = re.compile(_integer)
decimal_re = re.compile(r"{}(\.{})?|\.{}".format(_integer, _integer, _integer))

# Singleton metaclass

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Enumeration classes

class DefaultDeny(Enum):
    """Enumeration of NACM default deny values."""
    none = 1
    write = 2
    all = 3

class Axis(Enum):
    """Enumeration of implemented XPath axes."""
    ancestor = 1
    ancestor_or_self = 2
    attribute = 3
    child = 4
    descendant = 5
    descendant_or_self = 6
    following_sibling = 7
    parent = 8
    preceding_sibling = 9
    self = 10

class MultiplicativeOp(Enum):
    """Enumeration of XPath multiplicative operators."""
    multiply = 1
    divide = 2
    modulo = 3

class ContentType(Enum):
    """Enumeration of data content types."""
    config = 1
    nonconfig = 2
    all = 3
