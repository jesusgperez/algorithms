from typing import List, Optional

from pyfiles.base_bst import BaseBST
from pyfiles.domain import SegmentTreeNode


class SegmentTree(BaseBST):
    def __init__(self, nums: List[int]) -> None:
        super().__init__()
        self.build_tree(nums=nums)

    def build_tree(self, nums: List[int]) -> None:
        root = self._build_tree_recursive(nums=nums, end=len(nums)-1)
        self.root = root

    def _build_tree_recursive(
        self,
        nums: List[int],
        start: float = 0,
        end: float = 0
    ) -> Optional[SegmentTreeNode]:
        if start > end:
            return None

        node = SegmentTreeNode(indexes=(start, end))

        if start == end:
            try:
                node.data = nums[start]
            except IndexError:
                s = 0
                return
            return node

        mid = int(start + (end - start)/2)
        node.left = self._build_tree_recursive(nums=nums, start=start, end=mid)
        node.right = self._build_tree_recursive(nums=nums, start=mid+1, end=end)
        node.data = node.left.data + node.right.data

        return node
