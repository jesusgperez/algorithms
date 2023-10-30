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
