from abc import ABC, abstractmethod
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

    @abstractmethod
    def insert(self):
        pass
