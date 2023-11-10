from typing import Optional
from pyfiles.domain import CountTreeNode
from pyfiles.base_bst import BaseBST


class CountTree(BaseBST):
    """
        A tree structure to count the smaller numbers after self
        a good way found to do this is by creating a tree structure
        with slightly modified insertion method and an extra pointer
        to save the left count
    """
    def __init__(self) -> None:
        self.root = None
        self.n = 0
        self.inserted = {}

    def search(self, data: int) -> Optional[CountTreeNode]:
        if not data:
            return None

        try:
            self.inserted[data] += 1
        except KeyError:
            self.inserted[data] = 0

        return self._search_recursive(
            tree=self.root,
            data=data,
            skip=self.inserted[data]
        )

    def _search_recursive(
        self,
        tree: Optional[CountTreeNode],
        data: int,
        skip: int
    ) -> Optional[CountTreeNode]:
        if not tree:
            return tree

        if data < tree.data:
            return self._search_recursive(
                tree=tree.left,
                data=data,
                skip=skip
            )
        elif data > tree.data:
            return self._search_recursive(
                tree=tree.right,
                data=data,
                skip=skip
            )

        if skip:
            return self._search_recursive(
                tree=tree.right,
                data=data,
                skip=skip - 1
            )

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
            self.root = CountTreeNode(data=data, parent=parent)
            return self.root

        if not tree:
            return CountTreeNode(data=data, parent=parent)

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
