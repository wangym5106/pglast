# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from primnodes.h @ 10-1.0.2-0-gd710cb0
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2019 Lele Gaifax
#

from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *
from enum import IntEnum


class BoolExprType(IntEnum):
    AND_EXPR = 0
    OR_EXPR = 1
    NOT_EXPR = 2

class BoolTestType(IntEnum):
    IS_TRUE = 0
    IS_NOT_TRUE = 1
    IS_FALSE = 2
    IS_NOT_FALSE = 3
    IS_UNKNOWN = 4
    IS_NOT_UNKNOWN = 5

class CoercionContext(IntEnum):
    COERCION_IMPLICIT = 0
    COERCION_ASSIGNMENT = 1
    COERCION_EXPLICIT = 2

class CoercionForm(IntEnum):
    COERCE_EXPLICIT_CALL = 0
    COERCE_EXPLICIT_CAST = 1
    COERCE_IMPLICIT_CAST = 2

class MinMaxOp(IntEnum):
    IS_GREATEST = 0
    IS_LEAST = 1

class NullTestType(IntEnum):
    IS_NULL = 0
    IS_NOT_NULL = 1

class OnCommitAction(IntEnum):
    ONCOMMIT_NOOP = 0
    ONCOMMIT_PRESERVE_ROWS = 1
    ONCOMMIT_DELETE_ROWS = 2
    ONCOMMIT_DROP = 3

class ParamKind(IntEnum):
    PARAM_EXTERN = 0
    PARAM_EXEC = 1
    PARAM_SUBLINK = 2
    PARAM_MULTIEXPR = 3

class RowCompareType(IntEnum):
    ROWCOMPARE_LT = 1
    ROWCOMPARE_LE = 2
    ROWCOMPARE_EQ = 3
    ROWCOMPARE_GE = 4
    ROWCOMPARE_GT = 5
    ROWCOMPARE_NE = 6

class SQLValueFunctionOp(IntEnum):
    SVFOP_CURRENT_DATE = 0
    SVFOP_CURRENT_TIME = 1
    SVFOP_CURRENT_TIME_N = 2
    SVFOP_CURRENT_TIMESTAMP = 3
    SVFOP_CURRENT_TIMESTAMP_N = 4
    SVFOP_LOCALTIME = 5
    SVFOP_LOCALTIME_N = 6
    SVFOP_LOCALTIMESTAMP = 7
    SVFOP_LOCALTIMESTAMP_N = 8
    SVFOP_CURRENT_ROLE = 9
    SVFOP_CURRENT_USER = 10
    SVFOP_USER = 11
    SVFOP_SESSION_USER = 12
    SVFOP_CURRENT_CATALOG = 13
    SVFOP_CURRENT_SCHEMA = 14

class SubLinkType(IntEnum):
    EXISTS_SUBLINK = 0
    ALL_SUBLINK = 1
    ANY_SUBLINK = 2
    ROWCOMPARE_SUBLINK = 3
    EXPR_SUBLINK = 4
    MULTIEXPR_SUBLINK = 5
    ARRAY_SUBLINK = 6
    CTE_SUBLINK = 7

class XmlExprOp(IntEnum):
    IS_XMLCONCAT = 0
    IS_XMLELEMENT = 1
    IS_XMLFOREST = 2
    IS_XMLPARSE = 3
    IS_XMLPI = 4
    IS_XMLROOT = 5
    IS_XMLSERIALIZE = 6
    IS_DOCUMENT = 7

class XmlOptionType(IntEnum):
    XMLOPTION_DOCUMENT = 0
    XMLOPTION_CONTENT = 1


# #define-ed constants

INNER_VAR = 65000

OUTER_VAR = 65001

INDEX_VAR = 65002
