"""A reviewable CLI skeleton, not an implementation."""

import sys
from typing import Sequence


def make_slug(title: str) -> str:
    # R1/R2 pseudo: reject non-ASCII; lowercase; collapse each run of
    # non-alphanumerics to "-"; strip "-" from both ends; reject empty.
    # No I/O, external authorization, persistence or transactions.
    raise NotImplementedError("slug conversion not implemented")


def main(args: Sequence[str]) -> int:
    if len(args) != 1:
        print("expected one title", file=sys.stderr)
        return 2
    try:
        value = make_slug(args[0])
    except NotImplementedError as exc:
        print(exc, file=sys.stderr)
        return 3
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 2
    print(value)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
