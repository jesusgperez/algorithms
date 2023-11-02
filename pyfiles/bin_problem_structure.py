from typing import Optional
from pyfiles.avl_binary_tree import AVLBinaryTree
from pyfiles.domain import AVLTreeNode


class Bins(AVLBinaryTree):
    def __init__(self, capacity: int) -> None:
        super().__init__()
        self.capacity = capacity

    def get_best_fit(self, weight: float) -> Optional[AVLTreeNode]:
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
            Running log(n)
        """
        if not tree:
            return tree

        if self.capacity >= tree.data + weight:
            best_fit = self._is_space_for_recursive(
                tree=tree.right,
                weight=weight
            )

            if best_fit:
                return best_fit

            return tree

        return self._is_space_for_recursive(
            tree=tree.left,
            weight=weight
        )
