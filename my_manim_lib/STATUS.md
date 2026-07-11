# my_manim_lib — কোনটা ব্যবহার করবে, কোনটা সতর্ক

> এই ফাইলটা লাইব্রেরির সাথেই থাকে।  
> `pip install git+https://github.com/myabdur2121-cpu/my_manim_lib.git`  
> করলেই ডাউনলোড হয়ে যাবে — আগে থেকে সতর্কবার্তা পাবে।

সব ক্লাস **কোডে আছে এবং রান করে**। কিছু ক্লাস পুরোনো/দুর্বল/ডুপ্লিকেট —
তাই **মুছে ফেলা হয়নি** (পুরনো প্রজেক্ট যাতে না ভাঙে), শুধু নিচে মার্ক করা আছে।

---

## Animations

| Class | Status | Advice |
|-------|--------|--------|
| `ElasticSnapInOpacity` | ✅ Recommended | নতুন কোডে এটাই ব্যবহার করো |
| `ElasticSnapIn` | ⚠️ Legacy | opacity handling দুর্বল → `ElasticSnapInOpacity` নাও |
| `VectorFieldWarpIn` | ✅ Recommended | vectorized + introducer |
| `VectorFieldWarp` | ⚠️ Legacy | এর বদলে `VectorFieldWarpIn` |
| `StreamAlongPathIMG` | ✅ Recommended | image সহ path stream |
| `StreamAlongPath` | ⚠️ Legacy | কোড প্রায় identical → `StreamAlongPathIMG` |
| `FlyIntoPlaceholder` | ✅ Keep | FadeTransform দিয়ে placeholder-এ যায় |
| `ReplaceFlyIntoPlaceholder` | ✅ Keep | ReplacementTransform ভার্সন — দুটোই দরকার হতে পারে |
| `TrueSpiralInSubmobs` | ✅ Keep | |
| `ParticleDissolve` | ✅ Keep | |
| `SnappyPopIn` | ✅ Keep | |
| `FlySwap` | ✅ Keep | |
| `CreateWithFlash` | ✅ Keep | |
| `WordByWordCaption` | ✅ Keep | `SplitTex` / `SplitText` এর সাথে ভালো যায় |

---

## Mobjects

| Class | Status | Advice |
|-------|--------|--------|
| `GlowLine` | ✅ Keep | vector layered glow line |
| `GlowDot` | ✅ Keep | vector layered glow dot |
| `Glow` | ✅ Keep | any VMobject-এ glow |
| `BrightGlowDot` | ✅ Keep | pixel/image based bright glow |
| `MultiBrightGlow` | ✅ Keep | multiple shapes-এ image glow |
| `SmoothCross` | ✅ Keep | soft red X |
| `SplitTex` | ✅ Keep | word/letter split (LaTeX) |
| `SplitText` | ✅ Keep | word/letter split (Text) |
| `ScreenBlur` | ✅ Keep (fixed) | normal `Scene` + `MovingCameraScene` দুটোতেই কাজ করে |
| `TrueGaussianBlur2` | ✅ Keep (improved) | `sigma` + `intensity` দিয়ে মাত্রা কন্ট্রোল; true filled raster blur না, glow-style |

### TrueGaussianBlur2 quick guide
```python
TrueGaussianBlur2(shape, sigma=4,  intensity=1.0)   # subtle
TrueGaussianBlur2(shape, sigma=12, intensity=1.0)   # medium
TrueGaussianBlur2(shape, sigma=20, intensity=1.4)   # soft + strong
```

### ScreenBlur quick guide
```python
# normal Scene — works
blur = ScreenBlur(self, sigma=12)
self.play(FadeIn(blur))

# MovingCameraScene — also works
```

---

## কেন মুছে ফেলা হয়নি?

একবার কোনো ক্লাস ডিলিট করলে:
- পুরনো স্ক্রিপ্ট `ImportError` দেবে
- কোন ভার্সন কেন বাদ গেল মনে থাকবে না

তাই **সব রেখে STATUS নোট** রাখা ভালো।  
নতুন প্রজেক্টে শুধু ✅ Recommended / Keep ব্যবহার করো; ⚠️ Legacy এড়িয়ে চলো।
