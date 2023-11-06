from unittest import TestCase
from pyfiles.segment_tree import SegmentTree


class TestSegmentTree(TestCase):
    def test__build_tree__success(self):
        array = [2, 4, 6, 8]

        tree = SegmentTree(nums=array)

        self.assertEqual(tree.root.data, 20)
