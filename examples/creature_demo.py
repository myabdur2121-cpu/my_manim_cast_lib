"""
Demo: CustomCreature look + blink.

  manim -ql examples/creature_demo.py CreatureDemo
"""

from manim import *
from my_manim_lib import CustomCreature, list_creature_svgs


class CreatureDemo(Scene):
    def construct(self):
        # show which SVGs are installed
        modes = list_creature_svgs()
        label = Text(f"modes: {modes}", font_size=22).to_edge(UP)

        big_number = Text("1", font_size=180, color=BLUE)
        big_number.to_edge(LEFT, buff=1.5)

        creature = CustomCreature(mode="hands_up")
        creature.scale(2.5)
        creature.to_edge(RIGHT, buff=1)

        self.add(label, big_number, creature)

        target_point = big_number.get_center()
        self.play(creature.get_look_animation(target_point))
        self.wait(1.2)

        blink_close, blink_open = creature.get_blink_animation()
        self.play(blink_close)
        self.play(blink_open)
        self.wait(0.6)

        blink_close, blink_open = creature.get_blink_animation(duration=0.5)
        self.play(blink_close)
        self.play(blink_open)
        self.wait(1.0)
