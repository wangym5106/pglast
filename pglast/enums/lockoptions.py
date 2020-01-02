# -*- coding: utf-8 -*-
# :Project:   pglast -- DO NOT EDIT: automatically extracted from lockoptions.h @ 10-1.0.2-0-gd710cb0
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2017-2019 Lele Gaifax
#
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import *

from enum import Enum, IntEnum


class LockClauseStrength(IntEnum):
    LCS_NONE = 0
    LCS_FORKEYSHARE = 1
    LCS_FORSHARE = 2
    LCS_FORNOKEYUPDATE = 3
    LCS_FORUPDATE = 4

class LockWaitPolicy(IntEnum):
    LockWaitBlock = 0
    LockWaitSkip = 1
    LockWaitError = 2
