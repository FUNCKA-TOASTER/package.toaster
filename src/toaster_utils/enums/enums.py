"""Module "enums".

File:
    enums.py

About:
    File describing enums describing the data types
    of SQLAlchemy table columns.
"""

from enum import Enum


class PeerMark(Enum):
    """Description of peer mark types.

    Attributes:
        CHAT
        LOG
    """

    CHAT = "CHAT"
    LOG = "LOG"


class UserPermission(Enum):
    """Description of user access lvls.

    Attributes:
        user
        moderator
        administrator
    """

    user = 0
    moderator = 1
    administrator = 2


class SettingStatus(Enum):
    """Description of setting status.

    Attributes:
        active
        inactive
    """

    inactive = False
    active = True


class SettingDestination(Enum):
    """Description of setting destinations.

    Attributes:
        filter
        system
    """

    filter = "filter"
    system = "system"


class LinkType(Enum):
    """Description of link types.

    Attributes:
        domain
        url
    """

    domain = "domain"
    link = "link"


class LinkStatus(Enum):
    """Description of link status.

    Attributes:
        forbidden
        allowed
    """

    forbidden = "forbidden"
    allowed = "allowed"


class StaffRole(Enum):
    """Description of user staff roles.

    Attributes:
        ADM
        TECH
        SYS
    """

    ADM = "ADM"
    TECH = "TECH"
    SYS = "SYS"
