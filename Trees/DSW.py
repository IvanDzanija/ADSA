from BinaryTree import BinaryTree
from math import ceil, log


def DSW(tree: BinaryTree) -> None:
    root = tree.get_root()
    if root is None:
        return None

    tree.make_right_backbone()
    n = root.get_subtree_nodes_count()
    h = ceil(log(n + 1, 2))
    i = pow(2, h - 1) - 1
    DSW_rotates(tree, n - i)
    while i > 1:
        i = i // 2
        DSW_rotates(tree, i)
