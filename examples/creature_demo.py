"""
Demo scene for CustomCreature.

Run from repo root (after pip install -e .):
  manim -ql examples/creature_demo.py CreatureDemo
"""

from manim import *
from my_manim_lib import CustomCreature


class CreatureDemo(Scene):
    def construct(self):
        big_number = Text("1", font_size=180, color=BLUE)
        big_number.to_edge(LEFT, buff=1.5)

        creature = CustomCreature()
        creature.scale(2.5)
        creature.to_edge(RIGHT, buff=1)

        self.add(big_number, creature)

        target_point = big_number.get_center()

        # Look at the center of "1"
        self.play(creature.get_look_animation(target_point))
        self.wait(2)

        # First blink
        blink_close, blink_open = creature.get_blink_animation()
        self.play(blink_close)
        self.play(blink_open)
        self.wait(0.8)

        # Second blink
        blink_close, blink_open = creature.get_blink_animation(duration=0.5)
        self.play(blink_close)
        self.play(blink_open)
        self.wait(1.5)
