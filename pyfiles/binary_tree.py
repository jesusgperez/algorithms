from typing import Optional
from pydantic import BaseModel
from enum import Enum


class TreeTraversal(Enum):
    INORDER: str = 'inorder'
    PREORDER: str = 'preorder'
    POSTORDER: str = 'postorder'


class TreeNode(BaseModel):
    item: int
    parent: Optional['TreeNode'] = None
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

    def __repr__(self) -> str:
        parent_content = self.parent if not self.parent else self.parent.item
        right_content = self.right if not self.right else self.right.item
        left_content = self.left if not self.left else self.left.item
        return f'TreeNode(item={self.item}, parent={parent_content}, left={left_content}, right={right_content})'

    def __str__(self) -> str:
        return self.__repr__()


class RBinaryTree:
    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    def insert(self, new_item: int) -> TreeNode:
        return self._insert_recursive(new_item=new_item, tree=self.root)
    
    def _insert_recursive(
        self,
        new_item: int,
        tree: Optional[TreeNode],
        parent: Optional[TreeNode] = None
    ) -> TreeNode:
        if not self.root:
            self.root = TreeNode(item=new_item)
            return self.root

        if not tree:
            return TreeNode(item=new_item, parent=parent)
        else:
            if new_item < tree.item:
                tree.left = self._insert_recursive(new_item, tree.left, tree)
            else:
                tree.right = self._insert_recursive(new_item, tree.right, tree)

        return tree

    def traverse(self, traverse: TreeTraversal) -> str:
        if traverse not in list(TreeTraversal):
            raise ValueError('Invalid value for Tree Traversal')

        return self._traverse_tree_recursive(
            tree=self.root,
            traverse=traverse,
        )

    def _traverse_tree_recursive(
        self,
        tree: Optional[TreeNode],
        traverse: TreeTraversal
    ) -> str:
        result = ''
        if tree is None:
            return result

        if traverse == TreeTraversal.INORDER:
            result += self._traverse_tree_recursive(
                tree=tree.left,
                traverse=traverse
            )
            result += str(tree.item)
            result += self._traverse_tree_recursive(
                tree=tree.right,
                traverse=traverse
            )
        elif traverse == TreeTraversal.PREORDER:
            result += str(tree.item)
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
            result += str(tree.item)

        return result

    def get_depth(self) -> int:
        return self._get_depth_recursive(tree=self.root)

    def _get_depth_recursive(
        self,
        tree: Optional[TreeNode],
        depth: int = 0
    ) -> int:
        if not tree:
            return depth

        left_depth = self._get_depth_recursive(
            tree=tree.left,
            depth=depth+1
        )

        right_depth = self._get_depth_recursive(
            tree=tree.right,
            depth=depth+1
        )

        if depth > left_depth or depth > right_depth:
            return depth

        if left_depth > right_depth:
            return left_depth
        elif right_depth > left_depth:
            return right_depth

        return left_depth

    def search(self, item: int) -> Optional[TreeNode]:
        return self._search_recursive(tree=self.root, item=item)

    def _search_recursive(
        self,
        tree: Optional[TreeNode],
        item: int
    ) -> Optional[TreeNode]:
        if not tree or tree.item == item:
            return tree

        if item < tree.item:
            return self._search_recursive(tree=tree.left, item=item)

        return self._search_recursive(tree=tree.right, item=item)


class BinaryTree:
    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    def insert(self, new_item: int) -> str:
        if not self.root:
            self.root = TreeNode(item=new_item)
            return str(self.root)

        current: Optional[TreeNode] = self.root
        parent: Optional[TreeNode] = None

        while current:
            parent = current
            if new_item < current.item:
                current = current.left
            else:
                current = current.right

        new_node = TreeNode(item=new_item, parent=parent)
        
        if parent and new_item < parent.item:
            parent.left = new_node
        elif parent:
            parent.right = new_node

        return str(new_node)
    
    def traverse(self):
        pass
