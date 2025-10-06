from __future__ import annotations


class BinaryNode:
    height = -1
    parent = None

    def __init__(
        self, value, left: BinaryNode | None = None, right: BinaryNode | None = None
    ):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"BinaryNode({self.value})"

    def __str__(self):
        return str(self.value)

    def update_height(self) -> None:
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0

        self.height = 1 + max(left_height, right_height)

    # Getters and setters
    def get_height(self) -> int:
        self.update_height()
        return self.height

    def get_value(self):
        return self.value

    def set_value(self, value) -> None:
        self.value = value

    def get_left_child(self) -> BinaryNode | None:
        return self.left

    def set_left_child(self, left: BinaryNode | None) -> None:
        self.left = left
        if left is not None:
            left.set_parent(self)

    def get_right_child(self) -> BinaryNode | None:
        return self.right

    def set_right_child(self, right: BinaryNode | None) -> None:
        self.right = right
        if right is not None:
            right.set_parent(self)

    def get_parent(self) -> BinaryNode | None:
        return self.parent

    def set_parent(self, parent: BinaryNode) -> None:
        # This function can also be used to make a node as root but should be
        # avoided so we type hint it
        self.parent = parent

    # Avoid abusing this
    def make_root(self) -> None:
        self.parent = None

    def find_rightmost(self) -> BinaryNode | None:
        node = self.get_right_child()
        while node:
            if node.get_right_child():
                node = node.get_right_child()
            else:
                return node

    def find_leftmost(self) -> BinaryNode | None:
        node = self.get_left_child()
        while node:
            if node.get_left_child():
                node = node.get_left_child()
            else:
                return node

    # Essence of binary trees
    def query(self, value):
        if value < self.value and self.left:
            return self.left.query(value)
        elif value > self.value and self.right:
            return self.right.query(value)
        else:
            return self

    def get_child_count(self) -> int:
        left_child_count = 1 if self.left else 0
        right_child_count = 1 if self.right else 0
        return left_child_count + right_child_count

    def get_subtree_nodes_count(self) -> int:
        left_subtree_node_count = (
            self.left.get_subtree_nodes_count() if self.left else 0
        )
        right_subtree_node_count = (
            self.right.get_subtree_nodes_count() if self.right else 0
        )
        return 1 + left_subtree_node_count + right_subtree_node_count

    # Balancing factor is defined as BF(S) = h(R) - h(L)
    def balancing_factor(self):
        left_height, right_height = 0, 0
        if self.left is not None:
            left_height = self.left.get_height()
        if self.right is not None:
            right_height = self.right.get_height()
        return right_height - left_height

    def rotate_right(self, tree: BinaryTree) -> None:
        left_node = self.get_left_child()
        if left_node is None:
            return None
        parent_node = self.get_parent()
        if parent_node is None:
            left_node.make_root()
            tree.set_root(left_node)
        else:
            if parent_node.get_left_child() is self:
                parent_node.set_left_child(left_node)
            elif parent_node.get_right_child() is self:
                parent_node.set_right_child(left_node)

        temp = left_node.get_right_child()
        left_node.set_right_child(self)
        self.set_left_child(temp)

    def rotate_left(self, tree: BinaryTree) -> None:
        right_node = self.get_right_child()
        if right_node is None:
            return None
        parent_node = self.get_parent()
        if parent_node is None:
            right_node.make_root()
            tree.set_root(right_node)
        else:
            if parent_node.get_left_child() is self:
                parent_node.set_left_child(right_node)
            elif parent_node.get_right_child() is self:
                parent_node.set_right_child(right_node)
        temp = right_node.get_left_child()
        right_node.set_left_child(self)
        self.set_right_child(temp)


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
