"""Python utilities"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass


@dataclass
class Item:
    key: str
    value: str


def parse(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="shell-build", description="Python utilities")
    p.add_argument("--key", default="", help="item key")
    p.add_argument("--value", default="", help="item value")
    p.add_argument("--verbose", "-v", action="store_true")
    return p.parse_args(argv)


def run(args: argparse.Namespace) -> int:
    if args.verbose:
        print(f"key={args.key!r} value={args.value!r}", file=sys.stderr)
    if not args.key:
        print("nothing to do", file=sys.stderr)
        return 1
    item = Item(key=args.key, value=args.value)
    print(f"{item.key}={item.value}")
    return 0


def main() -> int:
    return run(parse())


if __name__ == "__main__":
    raise SystemExit(main())
