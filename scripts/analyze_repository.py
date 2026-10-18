
import os
import argparse
from collections import Counter
from pathlib import Path

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules"
}


def analyze_repository(root_path):
    """Analyze repository structure and summarize its files."""

    root = Path(root_path).resolve()

    if not root.exists() or not root.is_dir():
        raise ValueError(f"Invalid directory: {root_path}")

    file_list = []
    directory_list = []

    for current, directories, filenames in os.walk(root):
        directories[:] = sorted(
            d for d in directories if d not in EXCLUDED_DIRS
        )

        for directory in directories:
            directory_list.append(
                str(Path(current, directory).relative_to(root))
            )

        for filename in filenames:
            file_list.append(
                str(Path(current, filename).relative_to(root))
            )

    extensions = Counter(
        Path(filename).suffix.lower() or "No extension"
        for filename in file_list
    )

    python_files = [
        filename for filename in file_list
        if filename.lower().endswith(".py")
    ]

    return {
        "total_files": len(file_list),
        "total_directories": len(directory_list),
        "python_files": len(python_files),
        "extensions": dict(extensions),
        "python_file_list": python_files,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a software repository."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to the repository"
    )

    args = parser.parse_args()

    try:
        report = analyze_repository(args.path)
    except ValueError as error:
        parser.error(str(error))

    print("\n=== Repository Analysis Report ===")
    print(f"Total files       : {report['total_files']}")
    print(f"Total directories : {report['total_directories']}")
    print(f"Python files      : {report['python_files']}")

    print("\nFile Extensions:")
    for extension, count in sorted(report["extensions"].items()):
        print(f"  {extension}: {count}")

    print("\nPython Files:")
    for filename in report["python_file_list"]:
        print(f"  {filename}")

    print("\nAnalysis completed successfully!")


if __name__ == "__main__":
    main()
