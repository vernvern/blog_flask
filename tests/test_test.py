import unittest

class TestUnittest(unittest.TestCase):
    def test_one(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
