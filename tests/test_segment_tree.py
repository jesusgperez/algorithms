from unittest import TestCase
from data_structures.domain import SegmentTreeType
from data_structures.leetcode_problems.segment_tree import (
    SegmentTree,
    CountSegmentTree
)


class TestSegmentTree(TestCase):
    def test__build_tree__success(self):
        tree = SegmentTree(
            nums=[2, 4, 6, 8],
            tree_type=SegmentTreeType.SUM
        )

        self.assertEqual(tree.root.data, 20)

    def test__update_tree__success(self):
        tree = SegmentTree(
            nums=[2, 4, 6, 8],
            tree_type=SegmentTreeType.SUM
        )

        self.assertEqual(tree.root.data, 20)

        tree.update(index=1, data=5)

        self.assertEqual(tree.root.data, 21)

    def test__get_sum__success(self):
        tree = SegmentTree(
            nums=[2, 4, 6, 8],
            tree_type=SegmentTreeType.SUM
        )

        summed = tree.get_sum_range(start=1, end=3)
        self.assertEqual(summed, 18)

    def test__build_base_tree__success(self):
        tree = SegmentTree(
            tree_type=SegmentTreeType.BASE,
            min=1,
            max=6
        )

        self.assertEqual(tree.root.indexes, (1,6))

    def test__count_smaller__success(self):
        tree = CountSegmentTree(min=1, max=6)

        resp = tree.count_smaller(nums=[5, 2, 6, 1])

        self.assertEqual(resp, [2,1,1,0])

        tree = CountSegmentTree(min=-2, max=-1)

        resp = tree.count_smaller(nums=[-1, -2])

        self.assertEqual(resp, [1 ,0])
