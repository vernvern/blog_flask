import unittest


class TestTest1(unittest.TestCase):
    def test_1(self):
        print('-' * 100)
        print('test1')
        print('-' * 100)
        self.assertTrue(True)


def run():
    unittest.main()


if __name__ == '__main__':
    run()
