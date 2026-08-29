from __future__ import annotations

import argparse
from typing import Iterable

DEFAULT_NAME = "Hideot.iopr"


def repo_name(value: str | None = None) -> str:
    """Return the canonical repository name, stripping leading and trailing whitespace."""
    candidate = (value or DEFAULT_NAME).strip()
    return candidate or DEFAULT_NAME


def describe_project(name: str | None = None, *, status: str = "ready") -> dict[str, str]:
    """Build a basic metadata object for the project."""
    project_name = repo_name(name)
    return {
        "name": project_name,
        "status": status,
        "summary": f"{project_name} is {status}.",
    }


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Describe the Hideot.iopr project.")
    parser.add_argument("--name", default=DEFAULT_NAME, help="Project name to describe.")
    parser.add_argument("--status", default="ready", help="Current project status.")
    args = parser.parse_args(list(argv) if argv is not None else None)

    project = describe_project(args.name, status=args.status)
    print(project["summary"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
