from __future__ import annotations
from Nodes import BinaryNode


# This class does not provide support for duplicate value storage
class BinaryTree:
    root = None

    def __init__(self, values: list | None = None):
        if values is None:
            return None
        sorted_values = sorted(values)

        # Creates balanced binary tree from sorted list
        def _create_balanced_tree(values: list) -> BinaryNode | None:
            n = len(values)
            if n > 0:
                i = (n // 2) + (n % 2)
                root = BinaryNode(values[i - 1])
                root.set_left_child(_create_balanced_tree(values[0 : i - 1]))
                root.set_right_child(_create_balanced_tree(values[i:n]))
                return root
            else:
                return None

        self.root = _create_balanced_tree(sorted_values)

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

    def get_root(self) -> BinaryNode | None:
        return self.root

    def set_root(self, node: BinaryNode) -> None:
        self.root = node

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
            return None

        node_parent = node.get_parent()

        node_child_count = node.get_child_count()
        if node_child_count == 0:
            if node_parent is None:
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

            if node_parent is None:
                if node.get_left_child():
                    self.root = node.get_left_child()
                elif node.get_right_child():
                    self.root = node.get_right_child()

            elif node_parent.get_left_child() == node:
                node_parent.set_left_child(child_node)
            elif node_parent.get_right_child() == node:
                node_parent.set_right_child(child_node)

        # Found node has to have 2 child nodes
        else:
            assert node_child_count == 2
            # Deletion by copying
            pred_node = node.get_left_child()
            pred_node_value = None
            if pred_node is not None:
                pred_node_rightmost = pred_node.find_rightmost()
                if pred_node_rightmost is not None:
                    pred_node_value = pred_node_rightmost.get_value()
            # succ_node_value =
            # node.get_right_child().find_leftmost().get_value())
            assert pred_node_value is not None
            self.remove(pred_node_value)
            node.set_value(pred_node_value)

        def make_right_backbone(self):
            node = self.root
            while node is not None:
                temp = node.get_left_child()
                if temp is not None:
                    node.rotate_right()
                    node = temp
                else:
                    node = node.get_right_child()
