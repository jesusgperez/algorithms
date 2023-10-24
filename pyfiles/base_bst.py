from abc import ABC, abstractmethod
from typing import Optional
from domain import TreeNodeInterface


class BaseBST(ABC):
    def __init__(self):
        self.root: Optional[TreeNodeInterface] = None
        self.n: int = 0

    def search(self, data: int) -> Optional[TreeNodeInterface]:
        return self._search_recursive(data=data, tree=self.root)

    def _search_recursive(
        self,
        data: int, 
        tree: Optional[TreeNodeInterface]
    ) -> TreeNodeInterface:
        if not tree:
            return tree
        
        if tree.data < data:
            return self._search_recursive(data=data, tree=tree.left)

        return self._search_recursive(data=data, tree=tree.right)

    @abstractmethod
    def insert(self):
        pass
