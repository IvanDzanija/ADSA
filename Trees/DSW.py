from BinaryTree import BinaryTree
from math import ceil, log


class DSW:
    def __init__(self, tree: BinaryTree) -> None:
        self.tree = tree

    def DSW(self) -> None:
        if self.tree.get_root() is None:
            return None

        self.tree.make_right_backbone()
        root = self.tree.get_root()
        assert root is not None
        node_count = root.get_subtree_nodes_count()
        tree_height = int(log(node_count + 1, 2))
        inner_node_count = pow(2, tree_height) - 1
        leaf_count = node_count - inner_node_count
        self._DSW_rotate(leaf_count)
        i = inner_node_count
        while i > 1:
            i = i // 2
            self._DSW_rotate(i)

    def _DSW_rotate(self, node_count):
        node = self.tree.get_root()
        while node_count:
            node_count -= 1
            if node is not None:
                node_rc = node.get_right_child()
                node.rotate_left(self.tree)
                if node_rc is not None:
                    node = node_rc.get_right_child()
