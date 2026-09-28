"""
Aetrix-Lite

File:
    modes.py

Purpose:
    Defines the available Aetrix-Lite game modes.
"""

from enum import Enum


class GameMode(Enum):
    """
    Available Aetrix-Lite game modes.
    """

    ZEN = "ZEN"
    BLITZ = "BLITZ"
    FORTY_LINES = "40 LINES"
