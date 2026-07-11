# my_manim_lib

Custom **Manim Community** animations, mobjects, and multi-SVG creatures.

**Repo:** https://github.com/myabdur2121-cpu/my_manim_cast_lib

## Install

```bash
pip install git+https://github.com/myabdur2121-cpu/my_manim_cast_lib.git
```

Force reinstall after updates:

```bash
pip install --force-reinstall --no-deps git+https://github.com/myabdur2121-cpu/my_manim_cast_lib.git
```

Editable local install (development):

```bash
git clone https://github.com/myabdur2121-cpu/my_manim_cast_lib.git
cd my_manim_cast_lib
pip install -e .
```

## Quick start

```python
from manim import *
from my_manim_lib import *

class Demo(Scene):
    def construct(self):
        text = Text("Hello")
        self.play(ElasticSnapInOpacity(text))
        self.wait()
```

## Creatures (many SVGs — Pi-style modes)

SVGs live in `my_manim_lib/assets/creatures/`.

```python
from my_manim_lib import CustomCreature, list_creature_svgs

print(list_creature_svgs())              # ['hands_up', ...]
creature = CustomCreature(mode="hands_up").scale(2.5)

self.play(creature.get_look_animation(target.get_center()))
close, open_ = creature.get_blink_animation()
self.play(close)
self.play(open_)
```

Run the packaged demo:

```bash
manim -ql examples/creature_demo.py CreatureDemo
```

### নতুন pose / SVG যোগ (৩ ধাপ)

1. ফাইল রাখো: `my_manim_lib/assets/creatures/<mode_name>.svg`
2. অংশে stable **id** দাও (`head`, `left_eye`, `left_pupil`, `mouth`, …)
3. ব্যবহার: `CustomCreature(mode="<mode_name>")` — **নতুন Python class লাগে না**

পূর্ণ গাইড: [`my_manim_lib/creatures/README.md`](my_manim_lib/creatures/README.md)

## কোনটা ব্যবহার করবে? (সতর্কবার্তা)

| কোথায় | কী আছে |
|--------|--------|
| [`my_manim_lib/STATUS.md`](my_manim_lib/STATUS.md) | Recommended vs Legacy টেবিল |
| `animations.py` / `mobjects.py` উপরে | module docstring |
| Python | `import my_manim_lib; print(my_manim_lib.__status__)` |

### Recommended

- **Animations:** `ElasticSnapInOpacity`, `VectorFieldWarpIn`, `StreamAlongPathIMG`, `FlyIntoPlaceholder`, `ReplaceFlyIntoPlaceholder`, `TrueSpiralInSubmobs`, `ParticleDissolve`, `SnappyPopIn`, `FlySwap`, `CreateWithFlash`, `WordByWordCaption`
- **Mobjects:** `GlowLine`, `GlowDot`, `Glow`, `BrightGlowDot`, `MultiBrightGlow`, `SmoothCross`, `SplitTex`, `SplitText`, `ScreenBlur`, `TrueGaussianBlur2`
- **Creatures:** `CustomCreature`, `list_creature_svgs`

### Legacy (মুছে ফেলা হয়নি)

| Legacy | এর বদলে |
|--------|---------|
| `ElasticSnapIn` | `ElasticSnapInOpacity` |
| `VectorFieldWarp` | `VectorFieldWarpIn` |
| `StreamAlongPath` | `StreamAlongPathIMG` |

## Package layout

```text
my_manim_cast_lib/
├── examples/
│   └── creature_demo.py
├── my_manim_lib/
│   ├── __init__.py
│   ├── STATUS.md
│   ├── animations.py
│   ├── mobjects.py
│   ├── assets/
│   │   └── creatures/
│   │       └── hands_up.svg      ← add more SVGs here
│   └── creatures/
│       ├── README.md             ← how to add SVGs
│       ├── base.py               ← BaseCreature
│       ├── custom.py             ← CustomCreature
│       └── registry.py           ← optional mode docs
├── setup.py
├── MANIFEST.in
├── pyproject.toml
└── README.md
```

## Dependencies

- manim
- numpy
- scipy
- matplotlib

## License

Use freely for your Manim projects.
