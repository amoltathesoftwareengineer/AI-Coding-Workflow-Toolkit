
import tempfile
import unittest
from pathlib import Path

from scripts.analyze_repository import analyze_repository


class TestRepositoryAnalyzer(unittest.TestCase):

    def test_counts_repository_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            (root / "app.py").write_text(
                "print('Hello')",
                encoding="utf-8"
            )

            (root / "README.md").write_text(
                "# Test Project",
                encoding="utf-8"
            )

            report = analyze_repository(root)

            self.assertEqual(report["total_files"], 2)
            self.assertEqual(report["python_files"], 1)

    def test_detects_python_file(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            (root / "main.py").write_text(
                "x = 10",
                encoding="utf-8"
            )

            report = analyze_repository(root)

            self.assertIn(
                "main.py",
                report["python_file_list"]
            )

    def test_invalid_directory_raises_error(self):
        with self.assertRaises(ValueError):
            analyze_repository(
                "directory_that_does_not_exist_12345"
            )


if __name__ == "__main__":
    unittest.main()
