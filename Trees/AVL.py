from BinaryTree import BinaryTree, BinaryNode


def AVL(BinaryTree):
    def insert(self, value):
        new_node = super(self).insert(value)
        if new_node is not None:
            self.balance(new_node)

    def remove(self, value):
        removed_node_parent = super(self).remove(value)
        if removed_node_parent is not None:
            self.balance(removed_node_parent)

    def _balance(self, node: BinaryNode) -> None:
        node.update_height()
        node_parent = node.get_parent()
        if node.balancing_factor() in [-2, 2]:
            self._find_rotation_seq(node)
        if node_parent is not None:
            self._balance(node_parent)

    def _find_rotation_seq(self, node: BinaryNode):
        if node.balancing_factor() == 2:
            node_rc = node.get_right_child()
            if node_rc is not None:
                if node_rc.balancing_factor() in [0, 1]:
                    node.rotate_left(self)
                    self._update_heights([node, node_rc])
                elif node_rc.balancing_factor() == -1:
                    node_rc.rotate_right(self)
                    node.rotate_left(self)
                    self._update_heights([node_rc, node, node.get_parent()])
        return 0

    def _update_heights(self, node_list: list) -> None:
        for node in node_list:
            node.update_height()
