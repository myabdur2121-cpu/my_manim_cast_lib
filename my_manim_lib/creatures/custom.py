"""Concrete creature classes."""

from .base import BaseCreature


class CustomCreature(BaseCreature):
    """
    Main user-facing creature (stick figure SVG family).

    Examples
    --------
    >>> c = CustomCreature()                 # mode='hands_up'
    >>> c = CustomCreature(mode='hands_up')
    >>> self.play(c.get_look_animation(dot.get_center()))
    >>> close, open_ = c.get_blink_animation()
    >>> self.play(close); self.play(open_)
    """

    default_mode = "hands_up"
