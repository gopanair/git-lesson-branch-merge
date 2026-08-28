"""The whole test suite. Run it with: python3 test_greet.py"""

import json
import pathlib

from greet import GREETINGS, greet


def test_every_greeting_has_a_name_slot():
    for code, template in GREETINGS.items():
        assert "{name}" in template, f"{code} never says the person's name"


def test_english():
    assert greet("en", "Ada") == "Hello, Ada!"


def test_the_file_is_valid_json():
    path = pathlib.Path(__file__).parent / "greetings.json"
    json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    for name, fn in sorted(list(globals().items())):
        if name.startswith("test_"):
            fn()
            print(f"ok  {name}")
    print("\nAll good.")
