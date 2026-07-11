"""
my_manim_lib.creatures — SVG-based custom characters
====================================================

RECOMMENDED
  • CustomCreature — stick figure with look-at + blink helpers

Asset used
  my_manim_lib/assets/creature_hands_up_eyes_mouth.svg
"""

from pathlib import Path

import numpy as np
from manim import *

# Package-local SVG (works after pip install too)
_ASSETS_DIR = Path(__file__).resolve().parent / "assets"
CREATURE_HANDS_UP_SVG = _ASSETS_DIR / "creature_hands_up_eyes_mouth.svg"


class CustomCreature(SVGMobject):
    """Custom creature with eye tracking and blinking.

    Parts (from SVG order after dropping background rect):
      head, left_eye, right_eye, left_pupil, right_pupil,
      left_eyelid, right_eyelid, mouth
    """

    def __init__(self, file_name=None, **kwargs):
        if file_name is None:
            file_name = str(CREATURE_HANDS_UP_SVG)

        super().__init__(file_name=file_name, **kwargs)

        # Drop background rectangle if Manim imported it as a submobject
        self.submobjects = [
            mob for mob in self.submobjects if not isinstance(mob, Rectangle)
        ]

        submobs = self.submobjects
        # Indices assume the hands-up SVG layout (body paths + face parts)
        self.head = submobs[5]
        self.left_eye = submobs[6]
        self.right_eye = submobs[7]
        self.left_pupil = submobs[8]
        self.right_pupil = submobs[9]
        self.left_eyelid = submobs[10]
        self.right_eyelid = submobs[11]
        self.mouth = submobs[12]

        # Eyelids initially open
        self.left_eyelid.set_opacity(0)
        self.right_eyelid.set_opacity(0)

        # Eyelids render above pupils
        self.left_pupil.set_z_index(10)
        self.right_pupil.set_z_index(10)
        self.left_eyelid.set_z_index(20)
        self.right_eyelid.set_z_index(20)

    def _get_pupil_position(self, eye, pupil, target_point):
        """Calculate pupil position so the eye looks toward target_point."""
        eye_center = eye.get_center()
        direction = np.array(target_point, dtype=float) - eye_center
        direction[2] = 0

        distance = np.linalg.norm(direction[:2])
        if distance < 1e-8:
            return eye_center

        direction = direction / distance

        radius_x = max(0.01, (eye.width - pupil.width) / 2)
        radius_y = max(0.01, (eye.height - pupil.height) / 2)

        denominator = np.sqrt(
            (direction[0] / radius_x) ** 2 + (direction[1] / radius_y) ** 2
        )
        if denominator < 1e-8:
            return eye_center

        movement_factor = 0.88
        offset = direction / denominator * movement_factor
        return eye_center + offset

    def get_look_animation(self, target_point, run_time=0.6):
        """Make both pupils look at the target point."""
        left_pos = self._get_pupil_position(
            self.left_eye, self.left_pupil, target_point
        )
        right_pos = self._get_pupil_position(
            self.right_eye, self.right_pupil, target_point
        )
        return AnimationGroup(
            self.left_pupil.animate.move_to(left_pos),
            self.right_pupil.animate.move_to(right_pos),
            run_time=run_time,
        )

    def get_look_forward_animation(self, run_time=0.6):
        """Reset pupils to eye centers."""
        return AnimationGroup(
            self.left_pupil.animate.move_to(self.left_eye.get_center()),
            self.right_pupil.animate.move_to(self.right_eye.get_center()),
            run_time=run_time,
        )

    def get_blink_animation(self, duration=0.45):
        """Blink using only eyelid opacity. Returns (close, open) pair."""
        close = AnimationGroup(
            self.left_eyelid.animate.set_opacity(1),
            self.right_eyelid.animate.set_opacity(1),
            run_time=duration / 2,
        )
        open_eyes = AnimationGroup(
            self.left_eyelid.animate.set_opacity(0),
            self.right_eyelid.animate.set_opacity(0),
            run_time=duration / 2,
        )
        return close, open_eyes
