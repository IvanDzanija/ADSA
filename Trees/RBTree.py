from BinaryTree import BinaryTree


class RBTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        new_node = super().insert(value)
        node = None
        if new_node is None:
            node = self.get_root()
        else:
            new_node_lc = new_node.get_left_child()
            if new_node_lc is not None and new_node_lc.get_value() == value:
                node = new_node_lc
            else:
                node = new_node.get_right_child()
        node.set_color("red")
        self._restructure(node)

    def _restructure(self, node):
        return 0
