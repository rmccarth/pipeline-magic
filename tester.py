import unittest
import sample

class TestHello(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(sample.hello(), "hello from jenkins")


if __name__ == '__main__':
    unittest.main()