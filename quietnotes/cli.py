"""qn: add, list and drop notes."""
import sys
import time

from . import store


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if not args or args[0] == "list":
        for n in store.load():
            when = time.strftime("%d %b %H:%M", time.localtime(n["at"]))
            print(f"{n['id']:>3}  {when}  {n['text']}")
        return 0
    if args[0] == "add" and len(args) > 1:
        n = store.add(" ".join(args[1:]))
        print(f"added {n['id']}")
        return 0
    if args[0] == "drop" and len(args) == 2 and args[1].isdigit():
        ok = store.remove(int(args[1]))
        print("dropped" if ok else "no such note")
        return 0 if ok else 1
    print("usage: qn [list] | qn add <text> | qn drop <id>", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
