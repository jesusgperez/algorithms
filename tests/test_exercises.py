from unittest import TestCase
from algos.exercises import (
    binary_search,
    k_element_sum,
    unique_elements_array
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

    def test__unique_elements_array__success(self):
        array1 = [5, 6, 7, 8, 10, 12, 13]
        array2 = [1, 2, 3, 5, 8, 12]

        unique = unique_elements_array(array1=array1, array2=array2)

        self.assertEqual(unique, [1,2,3,5,6,7,8,10,12,13])
