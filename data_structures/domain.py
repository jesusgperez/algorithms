from enum import Enum
from pydantic import BaseModel
from typing import Optional, Tuple


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


class SegmentTreeType(Enum):
    BASE: str = 'base'
    SUM: str = 'sum'


class BaseTreeNode(BaseModel):
    data: float
    left: Optional['BaseTreeNode'] = None
    right: Optional['BaseTreeNode'] = None

    def __repr__(self):
        left_data = self.left.data if self.left else None
        right_data = self.right.data if self.right else None
        return f"TreeNode(data={self.data}, left={left_data}, right={right_data})"


class TreeNode(BaseTreeNode):
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


class AVLTreeNode(BaseTreeNode):
    left: Optional['AVLTreeNode'] = None
    right: Optional['AVLTreeNode'] = None
    height: int = 1
    left_count: int = 0

    def __repr__(self) -> str:
        right_content = self.right if not self.right else self.right.data
        left_content = self.left if not self.left else self.left.data
        return (f'TreeNode(data={self.data}, height={self.height}'
                f', left={left_content}, right={right_content})')

    def __str__(self) -> str:
        return self.__repr__()


class CountTreeNode(TreeNode):
    left_count: int = 0


class SegmentTreeNode(BaseModel):
    data: Optional[float] = None
    left: Optional['SegmentTreeNode'] = None
    right: Optional['SegmentTreeNode'] = None
    indexes: Tuple[int, int]

    def __repr__(self) -> str:
        left_content = self.left if not self.left else self.left.data
        right_content = self.right if not self.right else self.right.data
        return (f'TreeNode(data={self.data}, indexes={self.indexes}'
                f', left={left_content}, right={right_content})')

    def __str__(self) -> str:
        return self.__repr__()


class HeapChild(Enum):
    LEFT: int = 10
    RIGHT: int = 20
