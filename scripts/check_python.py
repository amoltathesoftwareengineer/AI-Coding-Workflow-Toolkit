
import argparse
import os
import py_compile
import tempfile
from pathlib import Path

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "build",
    "dist"
}


def find_python_files(root_path):
    """Find Python files without scanning excluded directories."""

    root = Path(root_path).resolve()

    if root.is_file() and root.suffix.lower() == ".py":
        return [root]

    if not root.exists() or not root.is_dir():
        raise ValueError(f"Invalid path: {root_path}")

    python_files = []

    for current, directories, filenames in os.walk(root):
        directories[:] = sorted(
            directory
            for directory in directories
            if directory not in EXCLUDED_DIRS
        )

        for filename in filenames:
            if filename.endswith(".py"):
                python_files.append(Path(current) / filename)

    return sorted(python_files)


def check_syntax(file_path):
    """Compile a Python file to detect syntax errors."""

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            output_file = Path(temp_dir) / "check.pyc"

            py_compile.compile(
                str(file_path),
                cfile=str(output_file),
                doraise=True
            )

        return True, "Syntax OK"

    except (py_compile.PyCompileError, OSError) as error:
        return False, str(error)


def main():
    parser = argparse.ArgumentParser(
        description="Check Python files for syntax errors."
    )

    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Python file or project directory"
    )

    args = parser.parse_args()

    try:
        files = find_python_files(args.path)
    except ValueError as error:
        parser.error(str(error))

    if not files:
        print("No Python files found.")
        return 0

    failures = 0

    print("\n=== Python Syntax Check ===")

    for file_path in files:
        passed, message = check_syntax(file_path)

        if passed:
            print(f"[PASS] {file_path.name}: {message}")
        else:
            failures += 1
            print(f"[FAIL] {file_path.name}: {message}")

    print(f"\nFiles checked: {len(files)}")
    print(f"Errors found: {failures}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
