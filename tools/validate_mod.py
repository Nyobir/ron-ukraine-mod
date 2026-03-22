"""
Validate Ukraine mod files for internal consistency.
Checks that all NAME/FROM/JUMP references in unitrules.xml resolve correctly,
and that no renamed keys break cross-file references.
"""
import xml.etree.ElementTree as ET
import os
import sys

GAME_DIR = os.path.join("C:", os.sep, "Program Files (x86)", "Steam", "steamapps", "common", "Rise of Nations")
MOD_DIR = os.path.join("C:", os.sep, "Projectsd", "ron-ukraine-mod")

errors = []
warnings = []

def check_unitrules():
    """Verify all FROM/JUMP references point to existing unit NAMEs."""
    path = os.path.join(MOD_DIR, "data", "unitrules.xml")
    tree = ET.parse(path)
    root = tree.getroot()

    # Collect all unit NAMEs (case-insensitive for matching, since the game engine is case-insensitive)
    unit_names = set()
    unit_names_lower = set()
    for unit in root.iter("UNIT"):
        name_el = unit.find("NAME")
        if name_el is not None and name_el.text:
            unit_names.add(name_el.text.strip())
            unit_names_lower.add(name_el.text.strip().lower())

    print(f"Found {len(unit_names)} unit definitions in unitrules.xml")

    # Check all FROM and JUMP references (case-insensitive, matching game behavior)
    for unit in root.iter("UNIT"):
        name_el = unit.find("NAME")
        unit_name = name_el.text.strip() if name_el is not None and name_el.text else "UNKNOWN"

        from_el = unit.find("FROM")
        if from_el is not None and from_el.text:
            ref = from_el.text.strip()
            if ref.lower() != "none" and ref.lower() not in unit_names_lower:
                errors.append(f"unitrules.xml: Unit '{unit_name}' has FROM='{ref}' which doesn't exist")

        jump_el = unit.find("JUMP")
        if jump_el is not None and jump_el.text:
            ref = jump_el.text.strip()
            if ref.lower() != "disable" and ref.lower() not in unit_names_lower:
                errors.append(f"unitrules.xml: Unit '{unit_name}' has JUMP='{ref}' which doesn't exist")

def check_unit_graphics_refs():
    """Verify unit NAMEs in unitrules.xml match what unit_graphics.xml expects."""
    unitrules_path = os.path.join(MOD_DIR, "data", "unitrules.xml")
    graphics_path = os.path.join(GAME_DIR, "Data", "unit_graphics.xml")

    if not os.path.exists(graphics_path):
        warnings.append(f"Cannot find {graphics_path} — skipping cross-reference check")
        return

    # Get all GRAPH values from mod unitrules (these are the keys that link to unit_graphics)
    tree = ET.parse(unitrules_path)
    root = tree.getroot()

    mod_units = {}
    for unit in root.iter("UNIT"):
        name_el = unit.find("NAME")
        graph_el = unit.find("GRAPH")
        if name_el is not None and graph_el is not None:
            name = name_el.text.strip() if name_el.text else ""
            graph = graph_el.text.strip() if graph_el.text else ""
            if graph:
                mod_units[name] = graph

    # Read unit_graphics.xml and find all UNIT name= attributes
    graphics_tree = ET.parse(graphics_path)
    graphics_root = graphics_tree.getroot()

    graphics_names = set()
    for unit_el in graphics_root.iter("UNIT"):
        name_attr = unit_el.get("name", "")
        if name_attr:
            # unit_graphics uses format like "RUSINYLANCER-DEFAULT-AGE0"
            base_name = name_attr.split("-")[0]
            graphics_names.add(base_name)

    # Check that all GRAPH values from our mod exist in unit_graphics
    for unit_name, graph_key in mod_units.items():
        if graph_key.upper() not in {g.upper() for g in graphics_names}:
            warnings.append(f"Unit '{unit_name}' has GRAPH='{graph_key}' not found in unit_graphics.xml")

def check_tribe_file():
    """Verify tribe file is well-formed."""
    path = os.path.join(MOD_DIR, "tribes", "russians.xml")
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        name = root.get("name", "")
        cities = root.findall(".//CITY")
        leaders = root.findall(".//LEADER")
        print(f"Tribe file: name='{name}', {len(leaders)} leaders, {len(cities)} cities")
        if len(cities) < 15:
            warnings.append(f"Only {len(cities)} cities — recommend 15+ for long games")
    except ET.ParseError as e:
        errors.append(f"tribes/russians.xml is malformed XML: {e}")

def check_rules():
    """Verify RUSSIAN_ power entries exist and have valid values."""
    path = os.path.join(MOD_DIR, "data", "rules.xml")
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    expected_keys = [
        "RUSSIAN_ATTRITION", "RUSSIAN_ATTRITION_UPGRADES", "RUSSIAN_OIL",
        "RUSSIAN_BORDERS", "RUSSIAN_BORDERS_PER_AGE", "RUSSIAN_COMMUNISM",
        "RUSSIAN_SPY_COST", "RUSSIAN_COSSACK_DAMAGE", "RUSSIAN_PLUNDER_STEAL",
        "RUSSIAN_FREE_CIVIC"
    ]
    for key in expected_keys:
        if key not in content:
            errors.append(f"rules.xml: Missing power entry '{key}'")
        else:
            print(f"  OK: {key} found")

def check_help():
    """Verify no stale Russian references in help.xml."""
    path = os.path.join(MOD_DIR, "data", "help.xml")
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    if "Russian Unique" in content:
        errors.append("help.xml: Still contains 'Russian Unique' text")
    if "Russian territory" in content:
        errors.append("help.xml: Still contains 'Russian territory' text")
    if "Power of the Motherland" in content:
        errors.append("help.xml: Still contains 'Power of the Motherland'")

    if "Ukraine" in content or "Ukrainian" in content:
        print("  OK: Ukrainian references found in help.xml")

def main():
    print("=== Ukraine Mod Validator ===\n")

    print("--- Checking tribe file ---")
    check_tribe_file()

    print("\n--- Checking rules.xml ---")
    check_rules()

    print("\n--- Checking unitrules.xml ---")
    check_unitrules()

    print("\n--- Checking unit_graphics cross-references ---")
    check_unit_graphics_refs()

    print("\n--- Checking help.xml ---")
    check_help()

    print("\n=== Results ===")
    if errors:
        print(f"\n ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
    if warnings:
        print(f"\n WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
    if not errors and not warnings:
        print("\n  All checks passed!")

    if errors:
        print(f"\n FAILED — {len(errors)} error(s) found. Fix before launching game.")
        sys.exit(1)
    else:
        print(f"\n PASSED — mod is safe to install.")
        sys.exit(0)

if __name__ == "__main__":
    main()
