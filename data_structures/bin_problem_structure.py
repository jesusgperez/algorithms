from typing import Optional
from data_structures.avl_binary_tree import AVLBinaryTree
from data_structures.domain import AVLTreeNode


class Bins(AVLBinaryTree):
    def __init__(self, capacity: int, precision: int = 2) -> None:
        super().__init__()
        self.capacity = capacity
        self.PRECISION = precision

    def pack(self, weight: float) -> None:
        """
        Runs 3*log(n) worst case
        """
        tree = self.get_best_fit(weight=weight)

        if tree:
            data = tree.data
            self.delete(data=data)
            new_data = round(data + weight, self.PRECISION)
            self.insert(data=new_data)
        else:
            self.insert(data=weight)

    def get_best_fit(self, weight: float) -> Optional[AVLTreeNode]:
        """
            Runs log(n)
        """
        return self._get_best_fit_recursive(
            tree=self.root,
            weight=weight
        )

    def _get_best_fit_recursive(
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
            best_fit = self._get_best_fit_recursive(
                tree=tree.right,
                weight=weight
            )

            if best_fit:
                return best_fit

            return tree

        return self._get_best_fit_recursive(
            tree=tree.left,
            weight=weight
        )
