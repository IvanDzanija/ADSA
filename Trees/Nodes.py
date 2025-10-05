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

    def get_right_child(self) -> BinaryNode | None:
        return self.right

    def set_right_child(self, right: BinaryNode | None) -> None:
        self.right = right

    def get_parent(self) -> BinaryNode | None:
        return self.parent

    def set_parent(self, parent: BinaryNode) -> None:
        # This function can also be used to make a noot as root but should be
        # avoided so we type hint it
        self.parent = parent

    # Avoid abusing this
    def make_root(self) -> None:
        self.parent = None

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
