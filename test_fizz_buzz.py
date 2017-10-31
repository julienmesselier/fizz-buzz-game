from unittest import TestCase
from fizz_buzz import *


class TestFizz_buzz(TestCase):
    def test_elements_count_should_be_100(self):
        self.assertEqual(100, len(fizz_buzz()))

    def test_1st_element_should_be_1(self):
        self.assertEqual('1', fizz_buzz()[0])

    def test_2nd_element_should_be_2(self):
        self.assertEqual('2', fizz_buzz()[1])

    def test_3rd_element_should_be_Fizz(self):
        self.assertEqual('Fizz', fizz_buzz()[2])

    def test_4th_element_should_be_4(self):
        self.assertEqual('4', fizz_buzz()[3])

    def test_5th_element_should_be_Buzz(self):
        self.assertEqual('Buzz', fizz_buzz()[4])

    def test_15th_element_should_be_FizzBuzz(self):
        self.assertEqual('FizzBuzz', fizz_buzz()[14])


class TestFizz_buzz_variations(TestCase):
    def test_variation_1_should_return_same_as_original_implementation(self):
        self.assertEqual(fizz_buzz_variation_1(), fizz_buzz())

    def test_variation_2_should_return_same_as_original_implementation(self):
        self.assertEqual(fizz_buzz_variation_2(), fizz_buzz())

    def test_variation_3_should_return_same_as_original_implementation(self):
        self.assertEqual(fizz_buzz_variation_3(), fizz_buzz())
