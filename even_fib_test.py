import unittest

from even_fib import get_even_fib


class TestEvenFib(unittest.TestCase):
    def test_simple_calculations(self):
        expected = [0, 2, 8, 34]
        actual = get_even_fib(4)
        self.assertListEqual(expected, actual)

        expected = [0, 2]
        actual = get_even_fib(2)
        self.assertListEqual(expected, actual)

        expected = [0, 2, 8]
        actual = get_even_fib(3)
        self.assertListEqual(expected, actual)

        expected = [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578, 14930352, 63245986]
        actual = get_even_fib(len(expected))
        self.assertListEqual(expected, actual)

    def test_corner_cases(self):
        expected = []
        actual = get_even_fib(0)
        self.assertListEqual(expected, actual)

        expected = []
        actual = get_even_fib(-1)
        self.assertListEqual(expected, actual)

        expected = [0]
        actual = get_even_fib(1)
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
