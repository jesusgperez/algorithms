from pyfiles.domain import (
    TreeNode,
    ListOptions,
    TreeTraversal
)
from typing import Optional, List, Tuple, Union
from pyfiles.double_linked_list import DLinkedList
from pyfiles.utils.utils import measure_time


class RBinaryTree:
    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None
        self.n: int = 0

    def insert(self, new_data: int) -> Optional[TreeNode]:
        if type(new_data) is not int:
            return None

        self.n += 1

        return self._insert_recursive(new_data=new_data, tree=self.root)

    def _insert_recursive(
        self,
        new_data: int,
        tree: Optional[TreeNode],
        parent: Optional[TreeNode] = None
    ) -> TreeNode:
        if not self.root:
            self.root = TreeNode(data=new_data)
            return self.root

        if not tree:
            return TreeNode(data=new_data, parent=parent)

        if new_data < tree.data:
            tree.left = self._insert_recursive(new_data, tree.left, tree)
        else:
            tree.right = self._insert_recursive(new_data, tree.right, tree)

        return tree

    def insert_node(self, new_node: TreeNode) -> Optional[TreeNode]:
        if type(new_node) is not TreeNode:
            return None

        self.n += 1

        return self._insert_recursive_node(new_node=new_node, tree=self.root)

    def _insert_recursive_node(
        self,
        new_node: TreeNode,
        tree: Optional[TreeNode],
        parent: Optional[TreeNode] = None 
    ) -> TreeNode:
        if not self.root:
            self.root = new_node
            return self.root

        if not tree:
            new_node.parent = parent
            return new_node
    
        if new_node.data < tree.data:
            tree.left = self._insert_recursive_node(
                new_node=new_node,
                tree=tree.left,
                parent=tree
            )
        else:
            tree.right = self._insert_recursive_node(
                new_node=new_node,
                tree=tree.right,
                parent=tree
            )

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
            return ''

        if traverse == TreeTraversal.INORDER:
            result += self._traverse_tree_recursive(
                tree=tree.left,
                traverse=traverse
            )
            result += '-' + str(tree.data)
            result += self._traverse_tree_recursive(
                tree=tree.right,
                traverse=traverse
            )
        elif traverse == TreeTraversal.PREORDER:
            result += '-' + str(tree.data)
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
            result += '-' + str(tree.data)

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

    def search(self, data: int) -> Optional[TreeNode]:
        return self._search_recursive(tree=self.root, data=data)

    def _search_recursive(
        self,
        tree: Optional[TreeNode],
        data: int
    ) -> Optional[TreeNode]:
        if not tree or tree.data == data:
            return tree

        if data < tree.data:
            return self._search_recursive(tree=tree.left, data=data)

        return self._search_recursive(tree=tree.right, data=data)

    def find_swapped(self) -> List[str]:
        traverse = self.traverse(TreeTraversal.INORDER).replace('-', '')
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
        dlist.append(tree.data)
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
        array.append(tree.data)
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

    def get_successor(self, data: int) -> Optional[TreeNode]:
        node = self.search(data=data)
        if not node:
            return None

        if node.right:
            return self.find_minimum(node=node.right)
        
        parent = node.parent

        while parent and node == parent.right:
            node = parent
            parent = node.parent

        return parent

    def get_predecessor(self, data: int) -> Optional[TreeNode]:
        node = self.search(data=data)
        if not node:
            return None
        
        if node.left:
            return self.find_maximum(node=node.left)
        
        parent = node.parent

        while parent and node == parent.left:
            node = parent
            parent = node.parent

        return parent

    def find_minimum(self, node: TreeNode = None) -> Optional[TreeNode]:
        if not node:
            node = self.root

        while node.left:
            node = node.left

        return node

    def find_maximum(self, node: TreeNode = None) -> Optional[TreeNode]:
        if not node:
            node = self.root

        while node.right:
            node = node.right
        
        return node

    def get_median(self) -> int:
        traverse = self.traverse(
            traverse=TreeTraversal.INORDER
        ).replace('-', '')
        return int(traverse[self.n//2 - 1])
    
    def get_n(self) -> Optional[TreeNode]:
        return self._get_n_recursive(tree=self.root)

    def _get_n_recursive(
        self,
        tree: Optional[TreeNode]
    ) -> int:
        response = 0
        if not tree:
            return 0

        response += self._get_n_recursive(tree=tree.left)
        response += 1
        response += self._get_n_recursive(tree=tree.right)

        return response


class BinaryTree:
    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    def insert(self, new_data: int) -> str:
        if not self.root:
            self.root = TreeNode(data=new_data)
            return str(self.root)

        current: Optional[TreeNode] = self.root
        parent: Optional[TreeNode] = None

        while current:
            parent = current
            if new_data < current.data:
                current = current.left
            else:
                current = current.right

        new_node = TreeNode(data=new_data, parent=parent)

        if parent and new_data < parent.data:
            parent.left = new_node
        elif parent:
            parent.right = new_node

        return str(new_node)

    def traverse(self):
        pass
