"""Print installed creature SVG modes. Run: python examples/list_modes.py"""
from my_manim_lib import list_creature_svgs, CREATURE_MODES, describe_mode, ASSETS_DIR

print("ASSETS_DIR:", ASSETS_DIR)
print("modes:", list_creature_svgs())
for m in list_creature_svgs():
    print(f"  - {m}: {describe_mode(m)}")
print("registry keys:", sorted(CREATURE_MODES))
