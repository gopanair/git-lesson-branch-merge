#!/usr/bin/env python3
"""Print a greeting in the language you ask for.

Usage: python3 greet.py <language-code> <name>
"""

import json
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
GREETINGS = json.loads((HERE / "greetings.json").read_text(encoding="utf-8"))


def greet(language: str, name: str) -> str:
    template = GREETINGS.get(language)
    if template is None:
        known = ", ".join(sorted(GREETINGS))
        raise SystemExit(f"I don't know '{language}'. I know: {known}")
    return template.format(name=name)


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit(__doc__.strip())
    print(greet(sys.argv[1], sys.argv[2]))


if __name__ == "__main__":
    main()
