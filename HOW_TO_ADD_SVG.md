# নতুন Creature SVG কীভাবে যোগ করবে

৪০–৫০টা pose পর্যন্ত এই নিয়ম ফলো করো। **নতুন Python class লাগে না।**

## ১) ফাইল কোথায় রাখবে

```text
my_manim_lib/assets/creatures/<mode_name>.svg
```

উদাহরণ:

- `hands_up.svg` (আছে)
- `plain.svg`
- `wave.svg`
- `think.svg`
- `happy.svg`
- `sad.svg`
- `point_left.svg`

নাম: ছোট হাতের অক্ষর + underscore (`snake_case`), শুধু `.svg`।

## ২) SVG-তে id দাও (সবচেয়ে জরুরি)

প্রতিটা অ্যানিমেটেবল অংশে **stable id**:

| id | অংশ | look/blink-এর জন্য |
|----|------|---------------------|
| `torso` | শরীর | optional |
| `left_leg` / `right_leg` | পা | optional |
| `left_arm` / `right_arm` | হাত | optional |
| `head` | মাথা | optional |
| `left_eye` / `right_eye` | চোখের সাদা | **look-এর জন্য লাগে** |
| `left_pupil` / `right_pupil` | মণি | **look-এর জন্য লাগে** |
| `left_eyelid` / `right_eyelid` | পলক | **blink-এর জন্য লাগে** (শুরুতে `opacity="0"`) |
| `mouth` বা `mouth_path` | মুখ | optional |

### উদাহরণ (চোখ)

```svg
<ellipse id="left_eye" cx="185" cy="92" rx="11" ry="7.5" fill="#ffffff"/>
<circle id="left_pupil" cx="185" cy="92" r="4.5" fill="#1a252f"/>
<ellipse id="left_eyelid" cx="185" cy="90" rx="12" ry="8" fill="#2C3E50" opacity="0"/>
```

### Tips

- পুরো ক্যানভাস background rect রাখলেও সমস্যা নেই — auto-drop হয়।
- সব id না থাকলেও load হবে; শুধু missing part-এর helper skip/no-op হবে।
- **Index (`submobjects[5]`) ব্যবহার করো না** — ৫০টা ফাইলে ক্রম ভাঙবে।

## ৩) (Optional) registry নোট

`my_manim_lib/creatures/registry.py`:

```python
CREATURE_MODES = {
    "hands_up": "Default stick figure, arms raised",
    "wave": "One hand waving",   # ← নতুন লাইন
}
```

শুধু ডকুমেন্টেশন — ছাড়লেও `CustomCreature(mode="wave")` কাজ করবে।

## ৪) কোডে ব্যবহার

```python
from my_manim_lib import CustomCreature, list_creature_svgs

print(list_creature_svgs())  # installed poses

c = CustomCreature(mode="wave").scale(2)
self.add(c)
self.play(c.get_look_animation(target.get_center()))
close, open_ = c.get_blink_animation()
self.play(close)
self.play(open_)

# pose বদল (নতুন instance)
c2 = c.copy_with_mode("hands_up")
self.play(ReplacementTransform(c, c2))
```

## ৫) টেস্ট

```bash
pip install -e .
python -c "from my_manim_lib import list_creature_svgs, CustomCreature; print(list_creature_svgs()); print(CustomCreature(mode='wave'))"
manim -ql examples/creature_demo.py CreatureDemo
```

## ৬) GitHub-এ আপডেট

```bash
git add my_manim_lib/assets/creatures/<mode>.svg
# registry বদলালে:
git add my_manim_lib/creatures/registry.py
git commit -m "Add creature mode: <mode>"
git push origin main
```

ইনস্টল আবার:

```bash
pip install --force-reinstall --no-deps git+https://github.com/myabdur2121-cpu/my_manim_cast_lib.git
```

## Checklist (প্রতি নতুন SVG)

- [ ] ফাইল `assets/creatures/<mode>.svg`
- [ ] eyes/pupils/eyelids-এ id (look/blink চাইলে)
- [ ] `list_creature_svgs()`-এ নাম দেখা যায়
- [ ] `CustomCreature(mode="...")` crash করে না
- [ ] (optional) registry + commit/push
