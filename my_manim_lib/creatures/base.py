"""
Base creature system — flexible SVG character loading.

Design goals (Pi Creature style, but simpler & scalable for 40–50 SVGs)
---------------------------------------------------------------------
1. One SVG file per pose / mode  →  assets/creatures/<name>.svg
2. Parts are found by **SVG element id** (not fragile list index)
3. Optional parts are OK (missing mouth / arms won't crash)
4. New SVG = drop file + optional 2-line registry entry
5. Helpers: look-at, blink, smile path swap later, etc.

SVG authoring rules (important!)
--------------------------------
Every animatable part should have a stable ``id``:

  body group (optional):  id="body"
  torso                   id="torso"
  left_leg / right_leg    id="left_leg" / id="right_leg"
  left_arm / right_arm    id="left_arm" / id="right_arm"
  head                    id="head"
  left_eye / right_eye    id="left_eye" / id="right_eye"
  left_pupil / right_pupil id="left_pupil" / id="right_pupil"
  left_eyelid / right_eyelid id="left_eyelid" / id="right_eyelid"
  mouth                   id="mouth"   (or id="mouth_path")

Background rects (full-canvas) are auto-dropped.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple, Union

import numpy as np
from manim import *

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets" / "creatures"

# Standard part ids we try to bind on every creature
STANDARD_PART_IDS: Tuple[str, ...] = (
    "torso",
    "left_leg",
    "right_leg",
    "left_arm",
    "right_arm",
    "head",
    "left_eye",
    "right_eye",
    "left_pupil",
    "right_pupil",
    "left_eyelid",
    "right_eyelid",
    "mouth",
    "mouth_path",
)

# Aliases: SVG id → attribute name on the creature instance
PART_ALIASES: Dict[str, str] = {
    "mouth_path": "mouth",
}


def list_creature_svgs() -> List[str]:
    """Return stem names of all SVGs in assets/creatures/."""
    if not ASSETS_DIR.exists():
        return []
    return sorted(p.stem for p in ASSETS_DIR.glob("*.svg"))


def resolve_svg(name_or_path: Union[str, Path]) -> Path:
    """
    Resolve a mode name or path to an absolute SVG path.

    Examples
    --------
    resolve_svg("hands_up")
    resolve_svg("hands_up.svg")
    resolve_svg("/full/path/to/file.svg")
    """
    p = Path(name_or_path)
    if p.suffix.lower() == ".svg" and p.is_file():
        return p.resolve()

    stem = p.stem if p.suffix.lower() == ".svg" else p.name
    candidate = ASSETS_DIR / f"{stem}.svg"
    if candidate.is_file():
        return candidate.resolve()

    # also allow flat assets/ for backwards compatibility
    legacy = ASSETS_DIR.parent / f"{stem}.svg"
    if legacy.is_file():
        return legacy.resolve()

    raise FileNotFoundError(
        f"Creature SVG not found: {name_or_path!r}\n"
        f"Looked in: {ASSETS_DIR}\n"
        f"Available: {list_creature_svgs()}"
    )


class BaseCreature(SVGMobject):
    """
    SVG-based character with id-based part mapping + face helpers.

    Parameters
    ----------
    mode :
        SVG stem name under ``assets/creatures/`` (e.g. ``\"hands_up\"``),
        or a full path to an ``.svg`` file.
    drop_background :
        Remove full-frame background rectangles.
    part_ids :
        Extra SVG ids to bind as attributes (beyond STANDARD_PART_IDS).
    """

    # Subclasses can override default mode
    default_mode: str = "hands_up"

    def __init__(
        self,
        mode: Optional[str] = None,
        drop_background: bool = True,
        part_ids: Optional[Sequence[str]] = None,
        **kwargs,
    ):
        mode = mode or self.default_mode
        self.mode = mode
        self.svg_path = resolve_svg(mode)

        super().__init__(file_name=str(self.svg_path), **kwargs)

        if drop_background:
            self._drop_background_rects()

        # Build id → mobject map from SVG (Manim stores original_id sometimes)
        self._parts: Dict[str, VMobject] = {}
        self._bind_parts(part_ids)

        # Convenience attributes (None if missing)
        self.torso = self._parts.get("torso")
        self.left_leg = self._parts.get("left_leg")
        self.right_leg = self._parts.get("right_leg")
        self.left_arm = self._parts.get("left_arm")
        self.right_arm = self._parts.get("right_arm")
        self.head = self._parts.get("head")
        self.left_eye = self._parts.get("left_eye")
        self.right_eye = self._parts.get("right_eye")
        self.left_pupil = self._parts.get("left_pupil")
        self.right_pupil = self._parts.get("right_pupil")
        self.left_eyelid = self._parts.get("left_eyelid")
        self.right_eyelid = self._parts.get("right_eyelid")
        self.mouth = self._parts.get("mouth") or self._parts.get("mouth_path")

        self._init_face()

    # ------------------------------------------------------------------
    # Part binding
    # ------------------------------------------------------------------
    def _drop_background_rects(self) -> None:
        kept = []
        for mob in self.submobjects:
            if isinstance(mob, Rectangle):
                # likely full-canvas background
                continue
            kept.append(mob)
        self.submobjects = kept

    def _iter_named_mobjects(self) -> Iterable[Tuple[str, Mobject]]:
        """Yield (svg_id, mobject) for family members that have an id."""
        for mob in self.get_family():
            # Manim SVG import: path_id / original_id vary by version
            for attr in ("path_id", "original_id", "svg_id", "name"):
                val = getattr(mob, attr, None)
                if isinstance(val, str) and val and not val.startswith("SVGPath"):
                    yield val, mob
                    break

    def _bind_parts(self, extra_ids: Optional[Sequence[str]] = None) -> None:
        wanted = set(STANDARD_PART_IDS)
        if extra_ids:
            wanted.update(extra_ids)

        # 1) Prefer real SVG ids if Manim exposed them
        found_by_id: Dict[str, Mobject] = {}
        for svg_id, mob in self._iter_named_mobjects():
            if svg_id in wanted and svg_id not in found_by_id:
                found_by_id[svg_id] = mob

        # 2) Fallback: positional map for known hands_up layout
        #    (body: torso, Lleg, Rleg, Larm, Rarm, head,
        #     eyes: Leye, Reye, Lpupil, Rpupil, Leyelid, Reyelid, mouth)
        if len(found_by_id) < 5:
            fallback_order = [
                "torso",
                "left_leg",
                "right_leg",
                "left_arm",
                "right_arm",
                "head",
                "left_eye",
                "right_eye",
                "left_pupil",
                "right_pupil",
                "left_eyelid",
                "right_eyelid",
                "mouth",
            ]
            # leaf-ish submobjects in draw order
            leaves = [m for m in self.submobjects]
            for i, name in enumerate(fallback_order):
                if i < len(leaves) and name not in found_by_id:
                    found_by_id[name] = leaves[i]

        # Apply aliases and store
        for svg_id, mob in found_by_id.items():
            attr = PART_ALIASES.get(svg_id, svg_id)
            self._parts[attr] = mob
            # also keep original id key
            self._parts[svg_id] = mob

    def get_part(self, name: str) -> Optional[Mobject]:
        """Return a named part or None."""
        return self._parts.get(name)

    def require_part(self, name: str) -> Mobject:
        part = self.get_part(name)
        if part is None:
            raise AttributeError(
                f"Creature mode={self.mode!r} missing part id={name!r}. "
                f"Bound parts: {sorted(set(self._parts))} "
                f"SVG={self.svg_path}"
            )
        return part

    def _init_face(self) -> None:
        if self.left_eyelid is not None:
            self.left_eyelid.set_opacity(0)
            self.left_eyelid.set_z_index(20)
        if self.right_eyelid is not None:
            self.right_eyelid.set_opacity(0)
            self.right_eyelid.set_z_index(20)
        if self.left_pupil is not None:
            self.left_pupil.set_z_index(10)
        if self.right_pupil is not None:
            self.right_pupil.set_z_index(10)

    # ------------------------------------------------------------------
    # Face helpers
    # ------------------------------------------------------------------
    def _get_pupil_position(self, eye, pupil, target_point):
        eye_center = eye.get_center()
        direction = np.array(target_point, dtype=float) - eye_center
        direction[2] = 0.0

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
        offset = direction / denominator * 0.88
        return eye_center + offset

    def get_look_animation(self, target_point, run_time: float = 0.6):
        """Look both pupils toward target_point."""
        if not all(
            [
                self.left_eye,
                self.right_eye,
                self.left_pupil,
                self.right_pupil,
            ]
        ):
            return Wait(run_time)

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

    def get_look_forward_animation(self, run_time: float = 0.6):
        if not all([self.left_eye, self.right_eye, self.left_pupil, self.right_pupil]):
            return Wait(run_time)
        return AnimationGroup(
            self.left_pupil.animate.move_to(self.left_eye.get_center()),
            self.right_pupil.animate.move_to(self.right_eye.get_center()),
            run_time=run_time,
        )

    def get_blink_animation(self, duration: float = 0.45):
        """Return (close, open) animation pair using eyelid opacity."""
        if self.left_eyelid is None or self.right_eyelid is None:
            # no eyelids → tiny no-op pair so call sites still work
            return Wait(duration / 2), Wait(duration / 2)

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

    # ------------------------------------------------------------------
    # Mode switching (load another SVG pose into a new creature)
    # ------------------------------------------------------------------
    def copy_with_mode(self, mode: str, **kwargs) -> "BaseCreature":
        """Create another creature instance with a different SVG pose."""
        cls = type(self)
        new = cls(mode=mode, **kwargs)
        # match scale/position roughly
        new.match_height(self)
        new.move_to(self.get_center())
        return new

    def __repr__(self) -> str:
        parts = sorted({k for k in self._parts if k in STANDARD_PART_IDS or k == "mouth"})
        return f"{type(self).__name__}(mode={self.mode!r}, parts={parts})"
