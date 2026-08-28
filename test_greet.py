"""The whole test suite. Run it with: python3 test_greet.py

No pytest, no dependencies — so it runs the same on your laptop and in CI.
A failing test prints why and exits non-zero, which is all CI looks at.
"""

import json
import pathlib

from greet import GREETINGS, greet


def test_the_file_is_valid_json():
    path = pathlib.Path(__file__).parent / "greetings.json"
    json.loads(path.read_text(encoding="utf-8"))


def test_english_is_untouched():
    assert greet("en", "Ada") == "Hello, Ada!", "the English greeting changed"


def test_every_greeting_has_a_name_slot():
    for code, template in GREETINGS.items():
        assert "{name}" in template, (
            f"'{code}' is {template!r} — it never says the person's name, "
            "so greet() would print the same thing for everybody"
        )


def test_language_codes_are_two_letters():
    for code in GREETINGS:
        assert len(code) == 2 and code.isalpha() and code.islower(), (
            f"'{code}' is not a two-letter lowercase language code"
        )


def test_every_greeting_survives_formatting():
    for code in GREETINGS:
        greet(code, "Ada")


if __name__ == "__main__":
    failures = 0
    for name, fn in sorted(globals().items()):
        if not name.startswith("test_"):
            continue
        try:
            fn()
        except AssertionError as exc:
            failures += 1
            print(f"FAIL   {name}\n         {exc}")
        except Exception as exc:
            failures += 1
            print(f"ERROR  {name}\n         {exc.__class__.__name__}: {exc}")
        else:
            print(f"ok     {name}")
    if failures:
        print(f"\n{failures} failing. Nothing merges until this is green.")
        raise SystemExit(1)
    print("\nAll good.")
