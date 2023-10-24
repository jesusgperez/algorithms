from typing import Optional
from pyfiles.domain import AVLTreeNode
from pyfiles.base_bst import BaseBST


class AVLBinaryTree(BaseBST):
    def __init__(self) -> None:
        self.root: Optional[AVLTreeNode] = None
        self.n: int = 0

    def insert(self, data: int) -> Optional[AVLTreeNode]:
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

    def get_balance(self) -> int:
        if not self.root:
            return 0

        left_depth = self._get_depth_recursive(tree=self.root.left)
        right_depth = self._get_depth_recursive(tree=self.root.right)

        return left_depth - right_depth

    def get_node_balance(self, tree: Optional[AVLTreeNode]) -> int:
        if not tree:
            return 0

        balance = (self._get_depth_recursive(tree=tree.left) -
                   self._get_depth_recursive(tree=tree.right))

        return balance

    def get_height(self, tree: Optional[AVLTreeNode]) -> int:
        if not tree:
            return 0

        return tree.height

    def get_depth(self) -> int:
        return self._get_depth_recursive(tree=self.root)

    def _get_depth_recursive(
        self,
        tree: Optional[AVLTreeNode],
        depth: int = 0
    ) -> int:
        if not tree:
            return depth

        left_depth = self._get_depth_recursive(tree=tree.left, depth=depth+1)
        right_depth = self._get_depth_recursive(tree=tree.right, depth=depth+1)

        return max(depth, left_depth, right_depth)
