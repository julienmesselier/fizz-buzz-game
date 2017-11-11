import unittest
import fizz_buzz as fb


class TestEvaluate(unittest.TestCase):
    def test_multiple_of_3_should_return_Fizz(self):
        self.assertEqual('Fizz', fb.evaluate(6))

    def test_multiple_of_5_should_return_Fizz(self):
        self.assertEqual('Buzz', fb.evaluate(10))

    def test_multiple_of_3_and_5_should_return_Fizz(self):
        self.assertEqual('FizzBuzz', fb.evaluate(15))

    def test_other_ways(self):
        self.assertEqual('8', fb.evaluate(8))


class TestFizz_buzz(unittest.TestCase):
    def test_elements_count_should_be_100(self):
        self.assertEqual(100, len(fb.fizz_buzz_list()))


class TestFizz_buzz_variations(unittest.TestCase):
    def test_variation_1_should_return_same_as_original_implementation(self):
        self.assertEqual(fb.fizz_buzz_variation_1(), fb.fizz_buzz_list())

    def test_variation_2_should_return_same_as_original_implementation(self):
        self.assertEqual(fb.fizz_buzz_variation_2(), fb.fizz_buzz_list())


if __name__ == '__main__':
    unittest.main()
