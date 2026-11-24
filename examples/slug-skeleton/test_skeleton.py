from pathlib import Path
import subprocess
import sys
import unittest


class SkeletonContract(unittest.TestCase):
    def test_t3_stub_is_not_success(self):
        cli = Path(__file__).with_name("slug.py")
        result = subprocess.run(
            [sys.executable, "-B", str(cli), "Road Map 2027!"],
            capture_output=True, text=True, check=False, timeout=5,
        )
        self.assertEqual((result.returncode, result.stdout), (3, ""))
        self.assertIn("not implemented", result.stderr)
