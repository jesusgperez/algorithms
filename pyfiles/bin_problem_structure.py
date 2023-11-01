from typing import Optional
from pyfiles.avl_binary_tree import AVLBinaryTree
from pyfiles.domain import AVLTreeNode


class Bins(AVLBinaryTree):
    def __init__(self, capacity: int) -> None:
        super().__init__()
        self.capacity = capacity

    def is_space_for(self, weight: float) -> Optional[AVLTreeNode]:
        return self._is_space_for_recursive(
            tree=self.root,
            weight=weight
        )

    def _is_space_for_recursive(
        self,
        tree: Optional[AVLTreeNode],
        weight: float
    ) -> Optional[AVLTreeNode]:
        """
            Currently running O(n) worst case
        """
        if not tree or round(self.capacity - tree.data, 2) >= weight:
            return tree

        left_space = self._is_space_for_recursive(
            tree=tree.left,
            weight=weight
        )

        if left_space:
            return left_space

        right_space = self._is_space_for_recursive(
            tree=tree.right,
            weight=weight
        )

        return right_space
