import unittest
import sample

class TestHello(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(sample.hello(), "hello from jenkins")

    def test_parse(self):
        self.assertEqual(sample.parse('hello'), 'o')
        self.assertEqual(sample.parse('my definition is decent'), 't')

if __name__ == '__main__':
    unittest.main()