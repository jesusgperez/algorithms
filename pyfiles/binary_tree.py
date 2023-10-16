from typing import Optional, List, Tuple, Union
from pydantic import BaseModel
from enum import Enum
from pyfiles.double_linked_list import DLinkedList
from pyfiles.utils.utils import measure_time


class ListOptions(Enum):
    DLINKEDLIST = 'double_linked_list'
    ARRAY = 'array'


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
        return (f'TreeNode(item={self.item}, parent={parent_content}'
                f', left={left_content}, right={right_content})')

    def __str__(self) -> str:
        return self.__repr__()


class RBinaryTree:
    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None
        self.n: int = 0

    def insert(self, new_item: int) -> Optional[TreeNode]:
        if type(new_item) is not int:
            return None

        self.n += 1

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

    def find_swapped(self) -> List[str]:
        traverse = self.traverse(TreeTraversal.INORDER)
        swapped: List[str] = []
        count: int = 0

        for i in range(1, len(traverse)):
            if int(traverse[i]) < int(traverse[i-1]):
                count += 1
                if count == 1:
                    swapped.append(traverse[i-1])
                else:
                    swapped.append(traverse[i])

            if count == 2:
                break

        return swapped

    @measure_time
    def to_list(
        self,
        list_option: ListOptions = ListOptions.DLINKEDLIST
    ) -> Union[DLinkedList, List, None]:
        if list_option == ListOptions.DLINKEDLIST:
            return self._to_list_recursive(tree=self.root)

        return self._to_array_recursive(tree=self.root)

    def _to_list_recursive(
        self,
        tree: Optional[TreeNode],
    ) -> Optional[DLinkedList]:
        dlist = DLinkedList()

        if not tree:
            return None

        dlist.extend(dlist=self._to_list_recursive(tree=tree.left))
        dlist.append(tree.item)
        dlist.extend(dlist=self._to_list_recursive(tree=tree.right))

        return dlist

    def _to_array_recursive(
        self,
        tree: Optional[TreeNode]
    ) -> List[int]:
        array: List[int] = []

        if not tree:
            return array

        array.extend(self._to_array_recursive(tree=tree.left))
        array.append(tree.item)
        array.extend(self._to_array_recursive(tree=tree.right))

        return array

    @measure_time
    def is_balanced(self) -> bool:
        balanced, _ = self._is_balanced_recursive(self.root)
        return balanced

    def _is_balanced_recursive(
        self,
        tree: Optional[TreeNode]
    ) -> Tuple[bool, int]:
        if not tree:
            return True, 0

        left_balance, left_height = self._is_balanced_recursive(
            tree=tree.left
        )
        right_balance, right_height = self._is_balanced_recursive(
            tree=tree.right
        )

        height = max(left_height, right_height) + 1

        if not left_balance or not right_balance:
            return left_balance and right_balance, height

        if abs(left_height - right_height) > 1:
            return False, height

        return True, height

    def get_successor(self, item: int) -> Optional[TreeNode]:
        node = self.search(item=item)
        if not node:
            return None

        if node.right:
            return self.find_minimum(node=node.right)
        
        parent = node.parent

        while parent and node == parent.right:
            node = parent
            parent = node.parent

        return parent

    def get_predecessor(self, item: int) -> Optional[TreeNode]:
        node = self.search(item=item)
        if not node:
            return None
        
        if node.left:
            return self.find_maximum(node=node.left)
        
        parent = node.parent

        while parent and node == parent.left:
            node = parent
            parent = node.parent

        return parent

    def find_minimum(self, node: TreeNode) -> Optional[TreeNode]:
        while node.left:
            node = node.left

        return node

    def find_maximum(self, node: TreeNode) -> Optional[TreeNode]:
        while node.right:
            node = node.right
        
        return node


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
