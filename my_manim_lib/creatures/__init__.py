"""
my_manim_lib.creatures
======================

Flexible SVG creature system (Pi-creature style layout, simpler API).

Quick start
-----------
from my_manim_lib import CustomCreature, list_creature_svgs

c = CustomCreature()                 # assets/creatures/hands_up.svg
c = CustomCreature(mode="hands_up")  # same

# When you add more SVGs later:
# c = CustomCreature(mode="wave")

print(list_creature_svgs())          # see installed pose files
"""

from .base import (
    ASSETS_DIR,
    BaseCreature,
    STANDARD_PART_IDS,
    list_creature_svgs,
    resolve_svg,
)
from .custom import CustomCreature
from .registry import CREATURE_MODES, describe_mode, known_modes

__all__ = [
    "ASSETS_DIR",
    "BaseCreature",
    "CustomCreature",
    "CREATURE_MODES",
    "STANDARD_PART_IDS",
    "describe_mode",
    "known_modes",
    "list_creature_svgs",
    "resolve_svg",
]
