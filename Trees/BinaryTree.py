from __future__ import annotations
from Nodes import BinaryNode


# This class does not provide support for duplicate value storage
class BinaryTree:
    def __init__(self, root: BinaryNode | None = None):
        self.root = root

    def __str__(self) -> str:
        """Return a pretty string representation of the tree (rotated 90°)."""
        if self.root is None:
            return "(empty tree)"

        lines: list[str] = []

        def _build_lines(
            node: BinaryNode | None, level: int = 0, label: str = "Root:"
        ) -> None:
            if node is not None:
                _build_lines(node.get_right_child(), level + 1, "R──")
                lines.append("    " * level + f"{label} {node.get_value()}")
                _build_lines(node.get_left_child(), level + 1, "L──")

        _build_lines(self.root)
        return "\n".join(lines)

    def find_rightmost(self) -> BinaryNode | None:
        node = self.root
        if node is None:
            return None
        while node:
            if node.get_right_child():
                node = node.get_right_child()
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

    def remove(self, value) -> None:
        if self.root is None:
            print("Tree is empty, nothing to remove!")
            return None
        node = self.root.query(value)
        if node is None:
            print(f"Node with value: {value} doesn't exist in the tree")
        node_parent = node.get_parent()
        node_child_count = node.get_child_count()
        if node_child_count == 0:
            if node_parent is None:
                assert node == self.root
                self.root = None
            elif node_parent.get_left_child() == node:
                node_parent.set_left_child(None)
            elif node_parent.get_right_child() == node:
                node_parent.set_right_child(None)
        elif node_child_count == 1:
            child_node = (
                node.get_right_child()
                if node.get_right_child()
                else node.get_left_child()
            )
            if node_parent.get_left_child() == node:
                node_parent.set_left_child(child_node)
