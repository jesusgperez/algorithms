from enum import Enum
from typing import Optional
from pydantic import BaseModel


class Node(BaseModel):
    data: int
    next: Optional['Node'] = None
    previous: Optional['Node'] = None


class ListOptions(Enum):
    DLINKEDLIST = 'double_linked_list'
    ARRAY = 'array'


class TreeTraversal(Enum):
    INORDER: str = 'inorder'
    PREORDER: str = 'preorder'
    POSTORDER: str = 'postorder'


class TreeNodeInterface(BaseModel):
    data: int
    left: Optional['TreeNodeInterface'] = None
    right: Optional['TreeNodeInterface'] = None


class TreeNode(TreeNodeInterface):
    parent: Optional['TreeNode'] = None
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

    def __repr__(self) -> str:
        parent_content = self.parent if not self.parent else self.parent.data
        right_content = self.right if not self.right else self.right.data
        left_content = self.left if not self.left else self.left.data
        return (f'TreeNode(data={self.data}, parent={parent_content}'
                f', left={left_content}, right={right_content})')

    def __str__(self) -> str:
        return self.__repr__()


class AVLTreeNode(TreeNodeInterface):
    left: Optional['AVLTreeNode'] = None
    right: Optional['AVLTreeNode'] = None
    height: int = 1

    def __repr__(self) -> str:
        right_content = self.right if not self.right else self.right.data
        left_content = self.left if not self.left else self.left.data
        return (f'TreeNode(data={self.data}, height={self.height}'
                f', left={left_content}, right={right_content})')

    def __str__(self) -> str:
        return self.__repr__()
