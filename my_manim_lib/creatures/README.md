# Creatures — কীভাবে নতুন SVG যোগ করবে (৪০–৫০টা পর্যন্ত)

## ফোল্ডার নিয়ম

```text
my_manim_lib/
  assets/
    creatures/
      hands_up.svg      ← এখন আছে
      plain.svg         ← পরে যোগ
      wave.svg
      think.svg
      happy.svg
      ...
  creatures/
    base.py             ← BaseCreature (id mapping + look/blink)
    custom.py           ← CustomCreature
    registry.py         ← optional docs/aliases
    __init__.py
```

## নতুন pose যোগ (৩ ধাপ)

### ১) SVG ফাইল রাখো
`my_manim_lib/assets/creatures/<mode_name>.svg`

উদাহরণ: `wave.svg`, `sad.svg`, `point_left.svg`

### ২) SVG-তে **stable id** দাও (সবচেয়ে গুরুত্বপূর্ণ)

Inkscape / Figma / হাতে — প্রতিটা অ্যানিমেটেবল অংশে id:

| id | কী |
|----|-----|
| `torso` | শরীর |
| `left_leg` / `right_leg` | পা |
| `left_arm` / `right_arm` | হাত |
| `head` | মাথা |
| `left_eye` / `right_eye` | চোখের সাদা অংশ |
| `left_pupil` / `right_pupil` | মণি |
| `left_eyelid` / `right_eyelid` | পাতা (শুরুতে opacity=0) |
| `mouth` বা `mouth_path` | মুখ |

সব id না থাকলেও চলবে — যেগুলো আছে শুধু সেগুলো bind হবে।  
কিন্তু **look/blink** চাইলে eyes + pupils + eyelids লাগবে।

### ৩) (Optional) registry-তে এক লাইন
`creatures/registry.py` → `CREATURE_MODES` dict-এ:

```python
"wave": "One hand waving",
```

**কোড লেখা বাধ্যতামূলক না** — ফাইল থাকলেই:

```python
CustomCreature(mode="wave")
```

## ব্যবহার

```python
from my_manim_lib import CustomCreature, list_creature_svgs

print(list_creature_svgs())  # ['hands_up', 'wave', ...]

c = CustomCreature(mode="hands_up").scale(2)
self.play(c.get_look_animation(target.get_center()))
close, open_ = c.get_blink_animation()
self.play(close)
self.play(open_)

# অন্য pose-এর নতুন instance
c2 = c.copy_with_mode("wave")
self.play(ReplacementTransform(c, c2))
```

## কেন index (submobjects[5]) ব্যবহার করি না?
৪০–৫০ SVG-তে path ক্রম বদলায় → index ভেঙে যায়।  
**id-based mapping** = নতুন ফাইল যোগে পুরনো কোড না ভাঙে।

## Pi Creature ধারণার সাথে মিল
| 3b1b Pi Creature | আমাদের সিস্টেম |
|------------------|----------------|
| modes (plain, happy…) | `mode="..."` SVG files |
| body parts as attrs | `c.left_pupil`, `c.mouth`… |
| look / blink helpers | `get_look_animation`, `get_blink_animation` |
| SVG assets folder | `assets/creatures/` |

## পরে সহজে বাড়ানো যাবে
- mouth shape swap (happy/sad path)
- arm wave animation by part
- color themes (`set_color` on torso/head)
- multiple characters (`TeacherCreature`, `StudentCreature` subclasses)

শুধু নতুন SVG + same ids → বাকি API একই থাকবে।
