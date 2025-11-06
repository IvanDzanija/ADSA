from __future__ import annotations
from BinaryTree import BinaryNode, BinaryTree


class RBTree(BinaryTree):
    # 1. Nodes can be colored either red or black ,
    # 2. The root of the tree is colored black ,
    # 3. All leafs of the tree are black ,
    # 4. Both children of a red node are black ,
    # 5. Each path from any node of the tree to all his descendant leaves
    # passes through the same number of black nodes .
    def __init__(self):
        super().__init__()

    def insert(self, value) -> None:
        new_node = super().insert(value)
        if new_node is not None:
            new_node.set_color("red")
            self._restructure(new_node)

    def _restructure(self, node: BinaryNode | None) -> None:
        if node is None:
            return
        parent = node.get_parent()
        grandparent = parent.get_parent() if parent is not None else None
        while (
            parent is not None
            and parent.get_color() == "red"
            and grandparent is not None
        ):
            uncle = (
                grandparent.get_left_child()
                if grandparent.get_right_child() == parent
                else grandparent.get_right_child()
            )
            if uncle is not None and uncle.get_color() == "red":
                uncle.set_color("black")
                parent.set_color("black")
                grandparent.set_color("red")
                node = grandparent
            else:
                if grandparent.get_left_child() == parent:
                    if parent.get_left_child() == node:
                        grandparent.rotate_right(self)
                        parent.color, grandparent.color = (
                            grandparent.color,
                            parent.color,
                        )
                    else:
                        parent.rotate_left(self)
                        node = parent
                else:
                    if parent.get_right_child() == node:
                        grandparent.rotate_left(self)
                        parent.color, grandparent.color = (
                            grandparent.color,
                            parent.color,
                        )
                    else:
                        parent.rotate_right(self)
                        node = parent

            parent = node.get_parent() if node is not None else None
            grandparent = parent.get_parent() if parent is not None else None
        root = self.get_root()
        if root is not None:
            root.set_color("black")

    def __str__(self) -> str:
        if self.root is None:
            return "(empty tree)"

        def _node_str(node: BinaryNode, prefix: str = "", is_left: bool = True) -> str:
            if node is None:
                return ""
            color = "(R)" if node.get_color() == "red" else "(B)"
            res = (
                prefix
                + ("├── " if is_left else "└── ")
                + f"{node.get_value()}{color}\n"
            )
            left = node.get_left_child()
            right = node.get_right_child()
            if left or right:
                if left:
                    res += _node_str(
                        left, prefix + ("│   " if is_left else "    "), True
                    )
                if right:
                    res += _node_str(
                        right, prefix + ("│   " if is_left else "    "), False
                    )
            return res

        root_color = "(R)" if self.root.get_color() == "red" else "(B)"
        s = f"Root: {self.root.get_value()}{root_color}\n"
        left = self.root.get_left_child()
        right = self.root.get_right_child()
        if left:
            s += _node_str(left, "", True)
        if right:
            s += _node_str(right, "", False)
        return s
