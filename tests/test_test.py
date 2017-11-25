import unittest

class TestUnittest(unittest.TestCase):
    def test_one(self):
        self.assertTrue(True)
    def test_two(self):
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
