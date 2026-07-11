"""
my_manim_lib
============

Custom Manim animations, mobjects & SVG creatures.

📌 Status notes: my_manim_lib/STATUS.md
   import my_manim_lib; print(my_manim_lib.__status__)

📌 Creature SVG guide: my_manim_lib/creatures/README.md
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

LEGACY (still available):
  ElasticSnapIn -> ElasticSnapInOpacity
  VectorFieldWarp -> VectorFieldWarpIn
  StreamAlongPath -> StreamAlongPathIMG

MOBjects: Glow*, BrightGlow*, SmoothCross, SplitTex/Text,
  ScreenBlur, TrueGaussianBlur2

Creatures (flexible multi-SVG):
  CustomCreature(mode="hands_up")
  list_creature_svgs()  # see assets/creatures/*.svg
  Add new pose: drop SVG with standard ids into assets/creatures/

Full notes: STATUS.md + creatures/README.md
"""
