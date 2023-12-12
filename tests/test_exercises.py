from unittest import TestCase
from algos.exercises import (
    k_element_sum,
    binary_search
)


class TestExercises(TestCase):
    def test__k_element_sum__success(self):
        array = [1,2,3,4,5,6]
        self.assertTrue(k_element_sum(array=array, k=2, t=3))
        self.assertFalse(k_element_sum(array=array, k=3, t=3))
        self.assertTrue(k_element_sum(array=array, k=2, t=6))


    def test__binary_search__success(self):
        array = [1,2,3,4,5,6]
        self.assertTrue(binary_search(array=array, element=5))

        array = list(range(50))
        for i in range(50):
            self.assertTrue(binary_search(array=array, element=i))
        self.assertFalse(binary_search(array=array, element=51))
        self.assertFalse(binary_search(array=array, element=-1))
