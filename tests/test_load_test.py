import unittest

from scripts.load_test import is_local_target


class SafetyTests(unittest.TestCase):
    def test_local_targets(self):
        self.assertTrue(is_local_target("http://127.0.0.1:8080/health"))
        self.assertTrue(is_local_target("http://localhost:8080/"))
        self.assertFalse(is_local_target("https://example.com/"))
        self.assertFalse(is_local_target("file:///etc/passwd"))


if __name__ == "__main__":
    unittest.main()
