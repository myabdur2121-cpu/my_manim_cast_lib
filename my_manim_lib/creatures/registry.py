"""
Creature registry — map friendly names → SVG modes / classes.

When you add a new SVG:
  1. Save file as:  my_manim_lib/assets/creatures/<mode_name>.svg
  2. (Optional) add an entry in CREATURE_MODES below for docs/aliases
  3. Use:  CustomCreature(mode="<mode_name>")

No code change is *required* for a new pose if SVG ids follow the standard
list in base.py — registry is only for aliases + documentation.
"""

from __future__ import annotations

from typing import Dict, List

# mode_name → short description (documentation / discovery)
CREATURE_MODES: Dict[str, str] = {
    "hands_up": "Default stick figure, arms raised, eyes + mouth",
    # Add more as you create SVGs, e.g.:
    # "plain": "Neutral standing pose",
    # "wave": "One hand waving",
    # "think": "Hand on chin",
    # "happy": "Smile mouth variant",
    # "sad": "Frown mouth variant",
}


def known_modes() -> List[str]:
    return sorted(CREATURE_MODES.keys())


def describe_mode(mode: str) -> str:
    return CREATURE_MODES.get(mode, "(no description — still loadable if SVG exists)")
