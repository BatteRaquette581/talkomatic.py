"""
talkomatic.api.v1

A wrapper for the v1 Talkomatic REST API using dataclasses
to represent the data returned by the API.
"""

from .auth import API_AUTH_HEADERS, get_auth_bot_token
from .config import ServerConfig
from .emoji_list import emoji_list
from .health import ServerHealth
from .me import UserSession
from .offensive_words import WordFilter
from .rooms import get_rooms, get_room, can_join_room, RoomJoinStatus, create_room

__all__ = [
    "RoomJoinStatus",
    "ServerConfig",
    "ServerHealth",
    "UserSession",
    "WordFilter",
    "can_join_room",
    "create_room",
    "emoji_list",
    "get_auth_bot_token",
    "get_room",
    "get_rooms",
]
