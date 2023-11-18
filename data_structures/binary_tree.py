from typing import Optional, List, Tuple, Union
from data_structures.domain import (
    TreeNode,
    ListOptions,
    TreeTraversal
)
from data_structures.base_bst import BaseBST
from data_structures.double_linked_list import DLinkedList
from data_structures.utils.utils import measure_time


class RBinaryTree(BaseBST):
    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None
        self.n: int = 0

    def insert(self, data: int) -> Optional[TreeNode]:
        if type(data) is not int:
            return None

        self.n += 1

        return self._insert_recursive(data=data, tree=self.root)

    def _insert_recursive(
        self,
        data: int,
        tree: Optional[TreeNode],
        parent: Optional[TreeNode] = None
    ) -> TreeNode:
        if not self.root:
            self.root = TreeNode(data=data)
            return self.root

        if not tree:
            return TreeNode(data=data, parent=parent)

        if data < tree.data:
            tree.left = self._insert_recursive(data=data, tree=tree.left)
        else:
            tree.right = self._insert_recursive(data=data, tree=tree.right)

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

    def delete(self, data: int):
        return self._delete_recursive(tree=self.root, data=data)

    def _delete_recursive(
        self,
        tree: Optional[TreeNode],
        data: int
    ) -> Optional[TreeNode]:
        if not tree:
            return tree

        if tree.data > data:
            tree.left = self._delete_recursive(
                tree=tree.left,
                data=data
            )
        elif tree.data < data:
            tree.right = self._delete_recursive(
                tree=tree.right,
                data=data
            )

        if tree.left is None:
            temp = tree.right
            del tree
            return temp
        elif tree.right is None:
            temp = tree.left
            del tree
            return temp

        temp = self.get_min_node(tree=tree.right)
        tree.data = temp.data
        tree.right = self._delete_recursive(
            tree=tree.right,
            data=temp.data
        )

        return tree

    def create_from_orders_deprec(
        self,
        preorder: List[int],
        inorder: List[int]
    ) -> None:
        """
            This is not the solution
        """
        stack = []
        settled = {}
        count = 0
        i = 0
        previous: Optional[TreeNode] = None

        while i < len(preorder):
            node = TreeNode(data=preorder[i])
 
            if not previous:
                previous = node
                self.root = previous
                settled[preorder[i]] = 0
                i += 1
                continue

            previous.left = node
            stack.append(previous)
            previous = node

            if preorder[i] == inorder[count]:
                try:
                    settled[inorder[i+1]] += 1
                    count = i + 2
                except KeyError:
                    settled[inorder[i+1]] = 0
                    count = i + 1

                for _ in range(2):
                    if not stack:
                        continue

                    previous = stack.pop()
                    previous.right = TreeNode(data=preorder[i+1])
                    i += 1

                previous = previous.right

            settled[preorder[i]] = 0

            i += 1
