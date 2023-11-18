from abc import ABC
from typing import Optional, List
from data_structures.domain import (
    BaseTreeNode,
    TreeTraversal
)


class BaseBST(ABC):
    def __init__(self) -> None:
        self.root: Optional[BaseTreeNode] = None
        self.n: int = 0

    def search(self, data: int) -> Optional[BaseTreeNode]:
        return self._search_recursive(data=data, tree=self.root)

    def _search_recursive(
        self,
        data: int,
        tree: Optional[BaseTreeNode]
    ) -> Optional[BaseTreeNode]:
        if not tree or tree.data == data:
            return tree

        if data < tree.data:
            return self._search_recursive(data=data, tree=tree.left)

        return self._search_recursive(data=data, tree=tree.right)

    def get_depth(self) -> int:
        return self._get_depth_recursive(tree=self.root)

    def _get_depth_recursive(
        self,
        tree: Optional[BaseTreeNode],
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

    def get_node_balance(self, tree: Optional[BaseTreeNode]) -> int:
        if not tree:
            return 0

        balance = (self._get_depth_recursive(tree=tree.left) -
                   self._get_depth_recursive(tree=tree.right))

        return balance

    def get_min_node(
        self,
        tree: Optional[BaseTreeNode]
    ) -> Optional[BaseTreeNode]:
        if not tree or not tree.left:
            return tree

        return self.get_min_node(tree=tree.left)

    def get_max_node(
        self,
        tree: Optional[BaseTreeNode]
    ) -> Optional[BaseTreeNode]:
        if not tree or not tree.right:
            return tree

        return self.get_max_node(tree=tree.right)

    def is_valid(self) -> bool:
        return self._is_valid_recursive(tree=self.root)

    def _is_valid_recursive(self, tree: Optional[BaseTreeNode]) -> bool:
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

    def traverse(self, traverse: TreeTraversal) -> str:
        if traverse not in list(TreeTraversal):
            raise ValueError('Invalid value for Tree Traversal')

        return self._traverse_tree_recursive(
            tree=self.root,
            traverse=traverse,
        )

    def _traverse_tree_recursive(
        self,
        tree: Optional[BaseTreeNode],
        traverse: TreeTraversal
    ) -> str:
        result = ''
        if tree is None:
            return ''

        if traverse == TreeTraversal.INORDER:
            result += self._traverse_tree_recursive(
                tree=tree.left,
                traverse=traverse
            )
            result += '-' + str(int(tree.data))
            result += self._traverse_tree_recursive(
                tree=tree.right,
                traverse=traverse
            )
        elif traverse == TreeTraversal.PREORDER:
            result += '-' + str(int(tree.data))
            result += self._traverse_tree_recursive(
                tree=tree.left,
                traverse=traverse
            )
            result += self._traverse_tree_recursive(
                tree=tree.right,
                traverse=traverse
            )
        elif traverse == TreeTraversal.POSTORDER:
            result += self._traverse_tree_recursive(
                tree=tree.left,
                traverse=traverse
            )
            result += self._traverse_tree_recursive(
                tree=tree.right,
                traverse=traverse
            )
            result += '-' + str(int(tree.data))

        return result

    def create_from_orders(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> None:

        self.root = self._create_from_orders_recursive(
            preorder=preorder,
            inorder=inorder
        )

    def _create_from_orders_recursive(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[BaseTreeNode]:
        if not preorder or not inorder:
            return None

        data = preorder[0]
        root = BaseTreeNode(data=data)
        index = inorder.index(data)

        root.left = self._create_from_orders_recursive(
            preorder=preorder[1:index+1],
            inorder=inorder[:index]
        )
        root.right = self._create_from_orders_recursive(
            preorder=preorder[index+1:],
            inorder=inorder[index+1:]
        )

        return root
