from abc import ABC
from typing import Optional
from pyfiles.domain import TreeNodeInterface


class BaseBST(ABC):
    def __init__(self) -> None:
        self.root: Optional[TreeNodeInterface] = None
        self.n: int = 0

    def search(self, data: int) -> Optional[TreeNodeInterface]:
        return self._search_recursive(data=data, tree=self.root)

    def _search_recursive(
        self,
        data: int,
        tree: Optional[TreeNodeInterface]
    ) -> Optional[TreeNodeInterface]:
        if not tree or tree.data == data:
            return tree

        if data < tree.data:
            return self._search_recursive(data=data, tree=tree.left)

        return self._search_recursive(data=data, tree=tree.right)

    def get_depth(self) -> int:
        return self._get_depth_recursive(tree=self.root)

    def _get_depth_recursive(
        self,
        tree: Optional[TreeNodeInterface],
        depth: int = 0
    ) -> int:
        if not tree:
            return depth

        left_depth = self._get_depth_recursive(tree=tree.left, depth=depth+1)
        right_depth = self._get_depth_recursive(tree=tree.right, depth=depth+1)

        return max(depth, left_depth, right_depth)

    def get_balance(self) -> int:
        if not self.root:
            return 0

        left_depth = self._get_depth_recursive(tree=self.root.left)
        right_depth = self._get_depth_recursive(tree=self.root.right)

        return left_depth - right_depth

    def get_node_balance(self, tree: Optional[TreeNodeInterface]) -> int:
        if not tree:
            return 0

        balance = (self._get_depth_recursive(tree=tree.left) -
                   self._get_depth_recursive(tree=tree.right))

        return balance

    def get_min_node(
        self,
        tree: Optional[TreeNodeInterface]
    ) -> Optional[TreeNodeInterface]:
        if not tree or not tree.left:
            return tree

        return self.get_min_node(tree=tree.left)

    def get_max_node(
        self,
        tree: Optional[TreeNodeInterface]
    ) -> Optional[TreeNodeInterface]:
        if not tree or not tree.right:
            return tree

        return self.get_max_node(tree=tree.right)

    def is_valid(self) -> bool:
        return self._is_valid_recursive(tree=self.root)
    
    def _is_valid_recursive(self, tree: Optional[TreeNodeInterface]) -> bool:
        if not tree:
            return True

        if not tree.left and not tree.right:
            return True

        min_node = self.get_min_node(tree=tree.right)

        if min_node and tree.data >= min_node.data:
            return False

        max_node = self.get_max_node(tree=tree.left)

        if max_node and tree.data <= max_node.data:
            return False

        if not tree.left:
            if tree.data >= tree.right.data:
                return False
            return self._is_valid_recursive(tree=tree.right)

        if not tree.right:
            if tree.data <= tree.left.data:
                return False
            return self._is_valid_recursive(tree=tree.left)

        if tree.data <= tree.left.data or tree.data >= tree.right.data:
            return False

        left_valid = self._is_valid_recursive(tree=tree.left)
        right_valid = self._is_valid_recursive(tree=tree.right)

        if not left_valid or not right_valid:
            return False

        return True
