from unittest import TestCase
from pyfiles.domain import SegmentTreeType
from pyfiles.leetcode_problems.segment_tree import SegmentTree


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
