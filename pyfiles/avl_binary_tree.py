from typing import Optional
from pyfiles.domain import AVLTreeNode
from pyfiles.base_bst import BaseBST


class AVLBinaryTree(BaseBST):
    def __init__(self) -> None:
        self.root: Optional[AVLTreeNode] = None
        self.n: int = 0

    def insert(self, data: int) -> Optional[AVLTreeNode]:
        self.n += 1
        return self._insert_recursive(tree=self.root, data=data)

    def _insert_recursive(
        self,
        tree: Optional[AVLTreeNode],
        data: int
    ) -> Optional[AVLTreeNode]:
        if not self.root:
            self.root = AVLTreeNode(data=data)
            return self.root

        if not tree:
            return AVLTreeNode(data=data)

        if data < tree.data:
            tree.left_count += 1
            tree.left = self._insert_recursive(
                tree=tree.left,
                data=data
            )
        else:
            tree.right = self._insert_recursive(
                tree=tree.right,
                data=data
            )

        tree.height = 1 + max(
            self.get_height(tree=tree.left),
            self.get_height(tree=tree.right)
        )

        balance = self.get_node_balance(tree=tree)

        # Left-left case
        if balance > 1 and data < tree.left.data:
            return self.right_rotate(z=tree)

        # Right-right case
        elif balance < -1 and data > tree.right.data:
            return self.left_rotate(z=tree)

        # Left-right case
        elif balance > 1 and data > tree.left.data:
            tree.left = self.left_rotate(z=tree.left)
            return self.right_rotate(z=tree)

        # Right-left case
        elif balance < -1 and data < tree.right.data:
            tree.right = self.right_rotate(z=tree.right)
            return self.left_rotate(z=tree)

        return tree

    def left_rotate(
        self,
        z: Optional[AVLTreeNode]
    ) -> Optional[AVLTreeNode]:
        """
            :param z: The first unbalanced node
        """
        y = z.right
        T2 = y.left

        y.left, z.right = z, T2

        y.left_count += z.left_count + 1

        if z == self.root:
            self.root = y

        self.adjust_rotation_heights(y=y, z=z)

        return y

    def right_rotate(
        self,
        z: Optional[AVLTreeNode]
    ) -> Optional[AVLTreeNode]:
        """
            :param z: The first unbalanced node
        """
        y = z.left
        T2 = y.right

        y.right, z.left = z, T2

        z.left_count = z.left_count - y.left_count + T2.left_count

        if z == self.root:
            self.root = y

        self.adjust_rotation_heights(y=y, z=z)

        return y

    def adjust_rotation_heights(
        self,
        z: Optional[AVLTreeNode],
        y: Optional[AVLTreeNode]
    ) -> None:
        """
            :param z: First unbalanced tree node
            :param y: The z child to rotate
        """
        if z:
            z.height = 1 + max(
                self.get_height(z.left),
                self.get_height(z.right)
            )
        if y:
            y.height = 1 + max(
                self.get_height(y.left),
                self.get_height(y.right)
            )

    def get_height(self, tree: Optional[AVLTreeNode]) -> int:
        if not tree:
            return 0

        return tree.height
    
    def get_median(self) -> float:
        odd_n = self.n // 2 + 1
        if self.n % 2 == 1:
            return self._get_median_recursive(
                tree=self.root,
                n=self.n//2+1
            )

        left = self._get_median_recursive(tree=self.root, n=odd_n)
        right = self._get_median_recursive(tree=self.root, n=odd_n-1)
        return (left + right)/2

    def _get_median_recursive(
        self,
        tree: Optional[AVLTreeNode],
        n: int,
        carry_over: int = 0
    ) -> int:
        if not tree:
            return 0

        if tree.left_count + carry_over + 1 == n:
            return tree.data

        if n < tree.left_count + carry_over + 1:
            return self._get_median_recursive(
                tree=tree.left,
                n=n,
                carry_over=carry_over
            )
        else:
            return self._get_median_recursive(
                tree=tree.right,
                n=n,
                carry_over=tree.left_count + carry_over + 1
            )
