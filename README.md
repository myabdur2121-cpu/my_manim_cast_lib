# my_manim_lib

Custom **Manim Community** animations & mobjects.

## Install

```bash
pip install git+https://github.com/<YOUR_USER>/<YOUR_NEW_REPO>.git
```

Force reinstall (after updates):

```bash
pip install --force-reinstall --no-deps git+https://github.com/<YOUR_USER>/<YOUR_NEW_REPO>.git
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

## কোনটা ব্যবহার করবে? (সতর্কবার্তা)

প্যাকেজের ভিতরেই নোট আছে — ডাউনলোড/ইনস্টল করলেই পাবে:

| কোথায় | কী আছে |
|--------|--------|
| [`my_manim_lib/STATUS.md`](my_manim_lib/STATUS.md) | Recommended vs Legacy টেবিল |
| `animations.py` / `mobjects.py` উপরে | module docstring |
| Python | `import my_manim_lib; print(my_manim_lib.__status__)` |

### Recommended (নতুন কোডে এগুলোই)

- **Animations:** `ElasticSnapInOpacity`, `VectorFieldWarpIn`, `StreamAlongPathIMG`, `FlyIntoPlaceholder`, `ReplaceFlyIntoPlaceholder`, `TrueSpiralInSubmobs`, `ParticleDissolve`, `SnappyPopIn`, `FlySwap`, `CreateWithFlash`, `WordByWordCaption`
- **Mobjects:** `GlowLine`, `GlowDot`, `Glow`, `BrightGlowDot`, `MultiBrightGlow`, `SmoothCross`, `SplitTex`, `SplitText`, `ScreenBlur`, `TrueGaussianBlur2`

### Legacy (মুছে ফেলা হয়নি — পুরনো কোড যাতে না ভাঙে)

| Legacy | এর বদলে ব্যবহার করো |
|--------|---------------------|
| `ElasticSnapIn` | `ElasticSnapInOpacity` |
| `VectorFieldWarp` | `VectorFieldWarpIn` |
| `StreamAlongPath` | `StreamAlongPathIMG` |

## Notes

- `ScreenBlur` works on both normal `Scene` and `MovingCameraScene`
- `TrueGaussianBlur2` uses `sigma` (spread) + `intensity` (strength)

## Dependencies

- manim
- numpy
- scipy
- matplotlib

## License

Use freely for your Manim projects.
