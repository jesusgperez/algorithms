from typing import Optional
from pyfiles.avl_binary_tree import AVLBinaryTree
from pyfiles.domain import AVLTreeNode


class Bins(AVLBinaryTree):
    def __init__(self, capacity: int) -> None:
        super().__init__()
        self.capacity = capacity

    def is_space_for(self, weight: int) -> Optional[AVLTreeNode]:
        return self._is_space_for_recursive(
            tree=self.root,
            weight=weight
        )

    def _is_space_for_recursive(
        self,
        tree: Optional[AVLTreeNode],
        weight: int
    ) -> Optional[AVLTreeNode]:
        if not tree or self.capacity - tree.data >= weight:
            return tree
        
        if weight > tree.data:
            return self._is_space_for_recursive(
                tree=tree.left,
                weight=weight
            )
        else:
            return self._is_space_for_recursive(
                tree=tree.right,
                weight=weight
            )
