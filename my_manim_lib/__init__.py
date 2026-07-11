"""
my_manim_lib
============

Custom Manim animations & mobjects.

📌 কোন ক্লাস recommended / legacy — দেখো:
   my_manim_lib/STATUS.md
   (অথবা: import my_manim_lib; print(my_manim_lib.__status__))
"""

from .animations import *
from .mobjects import *
from .creatures import *

__status__ = """
RECOMMENDED animations:
  ElasticSnapInOpacity, VectorFieldWarpIn, StreamAlongPathIMG,
  FlyIntoPlaceholder, ReplaceFlyIntoPlaceholder,
  TrueSpiralInSubmobs, ParticleDissolve, SnappyPopIn,
  FlySwap, CreateWithFlash, WordByWordCaption

LEGACY (still available, prefer recommended instead):
  ElasticSnapIn          -> use ElasticSnapInOpacity
  VectorFieldWarp        -> use VectorFieldWarpIn
  StreamAlongPath        -> use StreamAlongPathIMG

MOBjects: GlowLine, GlowDot, Glow, BrightGlowDot, MultiBrightGlow,
  SmoothCross, SplitTex, SplitText, ScreenBlur, TrueGaussianBlur2

Creatures:
  CustomCreature  (SVG: assets/creature_hands_up_eyes_mouth.svg)
  helpers: get_look_animation, get_look_forward_animation, get_blink_animation

Full notes: my_manim_lib/STATUS.md
"""
