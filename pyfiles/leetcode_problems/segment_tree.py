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
            node.data = nums[start]
            return node

        mid = int((end + start)/2)
        node.left = self._build_tree_recursive(
            nums=nums,
            start=start,
            end=mid
        )
        node.right = self._build_tree_recursive(
            nums=nums,
            start=mid+1,
            end=end
        )
        node.data = node.left.data + node.right.data

        return node

    def update(
        self,
        index: int,
        data: float
    ) -> None:
        return self._update_recursive(
            tree=self.root,
            index=index,
            data=data
        )

    def _update_recursive(
        self,
        tree: Optional[SegmentTreeNode],
        index: int,
        data: float
    ) -> None:
        if not tree:
            return

        start, end = tree.indexes

        if start == end:
            tree.data = data
            return

        mid = (end + start)/2

        if index < mid:
            self._update_recursive(
                tree=tree.left,
                index=index,
                data=data
            )
        else:
            self._update_recursive(
                tree=tree.right,
                index=index,
                data=data
            )

        tree.data = tree.left.data + tree.right.data

    def get_sum_range(self, start: int, end: int) -> int:
        return self._get_sum_range_recursive(
            tree=self.root,
            start=start,
            end=end
        )
    
    def _get_sum_range_recursive(
        self,
        tree: Optional[SegmentTreeNode],
        start: int,
        end: int
    ) -> int:
        if not tree:
            return 0

        tree_start, tree_end = tree.indexes

        if tree_start == start and tree_end == end:
            return tree.data

        mid = int((tree_start + tree_end)/ 2)

        if end <= mid:
            return self._get_sum_range_recursive(
                tree=tree.left,
                start=start,
                end=end
            )
        elif start >= mid + 1:
            return self._get_sum_range_recursive(
                tree=tree.right,
                start=start,
                end=end
            )
        
        left_sum = self._get_sum_range_recursive(
            tree=tree.left,
            start=start,
            end=mid
        )
        right_sum = self._get_sum_range_recursive(
            tree=tree.right,
            start=mid+1,
            end=end
        )

        return left_sum + right_sum
