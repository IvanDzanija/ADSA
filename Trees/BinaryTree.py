from __future__ import annotations
from Nodes import BinaryNode


# This class does not provide support for duplicate value storage
class BinaryTree:
    def __init__(self, root: BinaryNode | None = None):
        self.root = root

    def find_rightmost(self) -> BinaryNode | None:
        node = self.root
        if node is None:
            return None
        while node:
            if node.get_righ_child():
                node = node.get_righ_child()
            else:
                return node

    def find_leftmost(self) -> BinaryNode | None:
        node = self.root
        if node is None:
            return None
        while node:
            if node.get_left_child():
                node = node.get_left_child()
            else:
                return node

    def binary_search(self, value) -> BinaryNode | None:
        if self.root is None:
            return None
        node = self.root.query(value)
        if node.get_value() == value:
            return node
        return None

    def insert(self, value) -> BinaryNode | None:
        new_node = BinaryNode(value)
        if self.root is None:
            self.root = new_node
        else:
            node = self.root.query(value)
            if value < node.value:
                node.set_left_child(new_node)
            elif value > node.value:
                node.set_right_child(new_node)
            else:
                print("Node with this value already exist in the tree.")
                return None
        return new_node
