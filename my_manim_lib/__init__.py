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

Full notes: my_manim_lib/STATUS.md
"""
