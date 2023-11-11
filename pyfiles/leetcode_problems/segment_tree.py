import math
from typing import List, Optional

from pyfiles.base_bst import BaseBST
from pyfiles.domain import SegmentTreeNode, SegmentTreeType


class SegmentTree(BaseBST):
    def __init__(
        self,
        tree_type: SegmentTreeType,
        **kwargs
    ) -> None:
        super().__init__()
        self.type = tree_type
        if self.type == SegmentTreeType.SUM:
            nums = kwargs.get('nums', [])
            self.build_sum_tree(nums=nums)
        elif self.type == SegmentTreeType.BASE:
            min_val = kwargs.get('min', 0)
            max_val = kwargs.get('max', 0)
            self.build_base_tree(min_val=min_val, max_val=max_val)

    def build_sum_tree(self, nums: List[int]) -> None:
        root = self._build_tree_recursive(nums=nums, end=len(nums)-1)
        self.root = root

    def build_base_tree(self, min_val: int, max_val: int) -> None:
        root = self._build_tree_recursive(start=min_val, end=max_val)
        self.root = root

    def _build_tree_recursive(
        self,
        nums: Optional[List[int]] = None,
        start: float = 0,
        end: float = 0
    ) -> Optional[SegmentTreeNode]:
        if start > end:
            return None

        node = SegmentTreeNode(indexes=(start, end))

        if start == end:
            if self.type == SegmentTreeType.SUM:
                node.data = nums[start]
            return node

        mid = math.floor((end + start)/2)

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

        if self.type == SegmentTreeType.SUM:
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
        """
            This function takes log(n) time complexity
        """
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
            tree_data = tree.data if tree.data else 0
            return tree_data

        mid = math.floor((tree_start + tree_end) / 2)

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


class CountSegmentTree(SegmentTree):
    def __init__(self, **kwargs) -> None:
        """
            Initialization time of a base segment tree takes O(log(n)) time
        """
        super().__init__(SegmentTreeType.BASE, **kwargs)
        self.min = kwargs.get('min', 0)
        self.max = kwargs.get('max', 0)

    def _update_recursive(
        self,
        tree: Optional[SegmentTreeNode],
        index: int
    ) -> None:
        """
            This function takes O(log(n)) time complexity
        """
        if not tree:
            return

        start, end = tree.indexes

        if start == index and end == index:
            current_data = tree.data if tree.data else 0
            tree.data = current_data + 1
            return

        mid = int((start + end)/2)

        if index <= mid:
            self._update_recursive(tree=tree.left, index=index)
        else:
            self._update_recursive(tree=tree.right, index=index)

        if not tree.left or not tree.right:
            return

        left_data = tree.left.data if tree.left.data else 0
        right_data = tree.right.data if tree.right.data else 0

        tree.data = left_data + right_data

    def count_smaller(self, nums: Optional[List[int]]) -> List[int]:
        """
            This function is running nlog(n) time complexity
            Running through all n elements times
            2*log(n) for updating and getting the sum range
        """
        if not nums or not len(nums):
            return []

        counts = []

        # Runs nlog(n)
        for i in range(len(nums) - 1, -1, -1):
            self._update_recursive(tree=self.root, index=nums[i])
            counts.append(self.get_sum_range(
                start=self.min,
                end=nums[i]-1)
            )

        return counts[::-1]
