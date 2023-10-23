from typing import Optional
from pyfiles.domain import AVLTreeNode


class AVLBinaryTree:
    def __init__(self) -> None:
        self.root: Optional[AVLTreeNode] = None
        self.n: int = 0

    def insert(self, data: int) -> None:
        return self._insert_recursive(tree=self.root, data=data)

    def _insert_recursive(
        self,
        tree: Optional[AVLTreeNode],
        data: int
    ) -> AVLTreeNode:
        if not self.root:
            self.root = AVLTreeNode(data=data)
        
        if data < tree.data:
            self._insert_recursive(tree=tree.left, data=data)
        else:
            self._insert_recursive(tree=tree.right, data=data)
        
        tree.height = 1 + max(
            self.get_height(tree=tree.left), 
            self.get_height(tree=tree.right)
        )

        balance = self._get_depth_recursive(tree=tree)

        ## Left-left case
        if balance > 1 and data < tree.left.data:
            return self.right_rotate(z=tree)
        
        ## Right-right case
        if balance < -1 and data > tree.right.data:
            return self.left_rotate(z=tree)
    
        ## Left-right case
        if balance > 1 and data > tree.left.data:
            tree.left = self.left_rotate(z=tree.left)
            return self.right_rotate(z=tree)
        
        ##Right-left case
        if balance < -1 and data < tree.right.data:
            tree.right = self.right_rotate(z=tree.right)
            return self.left_rotate(z=tree)

        return tree

    def left_rotate(self, z: AVLTreeNode) -> AVLTreeNode:
        y = z.right
        T2 = y.left

        y.left, z.right = z, T2

        self.adjust_rotation_heights(y=y, z=z)

        return y
    
    def right_rotate(self, z: AVLTreeNode) -> AVLTreeNode:
        y = z.left
        T2 = y.right

        y.right, z.left = z, T2

        self.adjust_rotation_heights(y=y, z=z)

        return y

    def adjust_rotation_heights(
        self,
        y: AVLTreeNode,
        z: AVLTreeNode
    ) -> None:
        z.height = 1 + max(
            self.get_height(z.left),
            self.get_height(z.right)
        )
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

    def get_height(self, tree: AVLTreeNode) -> int:
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
