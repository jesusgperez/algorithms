from typing import Optional, List
from pyfiles.domain import CountTreeNode


class CountTree:
    def __init__(self) -> None:
        self.root = None
        self.n = 0

    def search(self, data: int) -> Optional[CountTreeNode]:
        if not data:
            return None

        return self._search_recursive(tree=self.root, data=data)

    def _search_recursive(
        self,
        tree: Optional[CountTreeNode],
        data: int
    ) -> Optional[CountTreeNode]:
        if not tree:
            return tree

        if data < tree.data:
            return self._search_recursive(tree=tree.left, data=data)
        elif data > tree.data:
            return self._search_recursive(tree=tree.right, data=data)

        return tree

    def insert(self, data: int) -> Optional[CountTreeNode]:
        self.n += 1
        return self._insert_recursive(data=data, tree=self.root)

    def _insert_recursive(
        self,
        data: int,
        tree: Optional[CountTreeNode],
        parent: Optional[CountTreeNode] = None
    ) -> CountTreeNode:
        if not self.root:
            self.root = CountTreeNode(data=data, index=self.n, parent=parent)
            return self.root

        if not tree:
            return CountTreeNode(data=data, index=self.n, parent=parent)

        if data < tree.data:
            tree.left_count += 1
            tree.left = self._insert_recursive(
                data=data,
                tree=tree.left,
                parent=tree
            )
            if tree.right:
                tree.right = self._insert_recursive(
                    data=data,
                    tree=tree.right,
                    parent=tree
                )
        else:
            tree.right = self._insert_recursive(
                data=data,
                tree=tree.right,
                parent=tree
            )

        return tree
