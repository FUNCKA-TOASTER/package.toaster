"""Module "scripts".

File:
    session.py

About:
    File describing custom SQLA scripts associated
    with the menu sessions.
"""

from typing import List, Tuple
from sqlalchemy.orm import Session
from toaster.models import (
    Session as MenuSession,
    Delay,
    Peer,
)
from toaster.enums import PeerMark
from datetime import datetime, timedelta
from toaster import TOASTER


ExpiredSessions = List[Tuple[int, List[int]]]


@TOASTER.script(auto_commit=False, debug=True)
def open_menu_session(session: Session, bpid: int, cmid: int) -> None:
    setting = session.get(Delay, {"bpid": bpid, "setting": "menu_session"})
    delay = setting.delay if setting else 0
    expired = datetime.now() + timedelta(minutes=delay)
    new_menu_session = MenuSession(bpid=bpid, cmid=cmid, expired=expired)
    session.add(new_menu_session)
    session.commit()


@TOASTER.script(auto_commit=False, debug=True)
def close_menu_session(session: Session, bpid: int, cmid: int) -> None:
    menu_session = session.get(MenuSession, {"bpid": bpid, "cmid": cmid})
    session.delete(menu_session)
    session.commit()


@TOASTER.script(auto_commit=False, debug=True)
def get_expired_sessions(session: Session) -> ExpiredSessions:
    result = []
    peers = session.query(Peer).filter(Peer.mark == PeerMark.CHAT).all()

    if not peers:
        return result

    for peer in peers:
        cmids = []

        expired_sessions = (
            session.query(MenuSession)
            .filter(
                MenuSession.expired <= datetime.now(),
                MenuSession.bpid == peer.id,
            )
            .all()
        )

        if not expired_sessions:
            continue

        for expired_session in expired_sessions:
            cmids.append(expired_session.cmid)

        peer_expired_sessions = (peer.id, cmids)
        result.append(peer_expired_sessions)

    return result
