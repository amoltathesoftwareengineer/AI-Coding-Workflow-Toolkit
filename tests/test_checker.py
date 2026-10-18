
import tempfile
import unittest
from pathlib import Path

from scripts.check_python import (
    check_syntax,
    find_python_files,
)


class TestPythonSyntaxChecker(unittest.TestCase):

    def test_valid_python_code(self):
        with tempfile.TemporaryDirectory() as temp:
            file_path = Path(temp) / "valid.py"

            file_path.write_text(
                "total = 10 + 20\n",
                encoding="utf-8"
            )

            passed, message = check_syntax(file_path)

            self.assertTrue(passed)
            self.assertEqual(message, "Syntax OK")

    def test_invalid_python_code(self):
        with tempfile.TemporaryDirectory() as temp:
            file_path = Path(temp) / "invalid.py"

            file_path.write_text(
                "def broken(:\n",
                encoding="utf-8"
            )

            passed, message = check_syntax(file_path)

            self.assertFalse(passed)
            self.assertTrue(message)

    def test_discovers_python_files(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            (root / "app.py").write_text(
                "x = 1\n",
                encoding="utf-8"
            )

            (root / "README.md").write_text(
                "# Demo",
                encoding="utf-8"
            )

            python_files = find_python_files(root)

            self.assertEqual(len(python_files), 1)
            self.assertEqual(
                python_files[0].name,
                "app.py"
            )


if __name__ == "__main__":
    unittest.main()
