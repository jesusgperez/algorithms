from typing import Optional
from pyfiles.domain import TreeNode

class AVLBinaryTree:
    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None
        self.n: int = 0

    def insert(self, data) -> None:
        pass

    def get_balance(self) -> int:
        left_depth = self._get_depth_recursive(tree=self.root.left)
        right_depth = self._get_depth_recursive(tree=self.root.right)
        return abs(left_depth - right_depth)

    def get_depth(self):
        return self._get_depth_recursive(tree=self.root)
    
    def _get_depth_recursive(
        self,
        tree: Optional[TreeNode],
        depth: int = 0
    ) -> int:
        if not tree:
            return depth
        
        left_depth = self._get_depth_recursive(tree=tree.left, depth=depth+1)
        right_depth = self._get_depth_recursive(tree=tree.right, depth=depth+1)

        return max(depth, left_depth, right_depth)
