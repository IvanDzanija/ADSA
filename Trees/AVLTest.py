from BinaryTree import BinaryTree, BinaryNode
from AVL import AVL


def build_avl_tree():
    tree = AVL()
    return tree


def test_avl_single_right_rotation_ll_case():
    """
    LL rotation case:
            3
           /
          2
         /
        1
    should rebalance to:
          2
         / \
        1   3
    """
    tree = build_avl_tree()
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)

    root = tree.get_root()
    assert root is not None
    assert root.get_value() == 2
    lc, rc = root.get_left_child(), root.get_right_child()
    assert lc is not None and rc is not None
    assert lc.get_value() == 1
    assert rc.get_value() == 3
    assert root.balancing_factor() == 0


def test_avl_single_left_rotation_rr_case():
    """
    RR rotation case:
        1
         \
          2
           \
            3
    should rebalance to:
          2
         / \
        1   3
    """
    tree = build_avl_tree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)

    root = tree.get_root()
    assert root is not None
    assert root.get_value() == 2
    lc, rc = root.get_left_child(), root.get_right_child()
    assert lc is not None and rc is not None
    assert lc.get_value() == 1
    assert rc.get_value() == 3
    assert root.balancing_factor() == 0


def test_avl_left_right_rotation_lr_case():
    """
    LR rotation case:
          3
         /
        1
         \
          2
    should rebalance to:
          2
         / \
        1   3
    """
    tree = build_avl_tree()
    tree.insert(3)
    tree.insert(1)
    tree.insert(2)

    root = tree.get_root()
    assert root is not None
    assert root.get_value() == 2
    lc, rc = root.get_left_child(), root.get_right_child()
    assert lc is not None and rc is not None
    assert lc.get_value() == 1
    assert rc.get_value() == 3
    assert root.balancing_factor() == 0


def test_avl_right_left_rotation_rl_case():
    """
    RL rotation case:
        1
         \
          3
         /
        2
    should rebalance to:
          2
         / \
        1   3
    """
    tree = build_avl_tree()
    tree.insert(1)
    tree.insert(3)
    tree.insert(2)

    root = tree.get_root()
    assert root is not None
    assert root.get_value() == 2
    lc, rc = root.get_left_child(), root.get_right_child()
    assert lc is not None and rc is not None
    assert lc.get_value() == 1
    assert rc.get_value() == 3
    assert root.balancing_factor() == 0


def test_avl_no_rebalance_needed():
    tree = build_avl_tree()
    for val in [2, 1, 3]:
        tree.insert(val)

    root = tree.get_root()
    assert root is not None
    assert root.get_value() == 2
    assert root.balancing_factor() == 0
    assert root.get_height() == 2


def test_avl_correctly_insert_textbook():
    tree = build_avl_tree()
    for val in [16, 29, 18, 34, 26, 15, 45, 33, 6, 37, 49, 48, 40]:
        tree.insert(val)

    root = tree.get_root()
    assert root is not None
    assert root.get_value() == 34
    assert root.balancing_factor() == 0
    assert root.get_height() == 4
    rc, lc = root.get_right_child(), root.get_left_child()
    assert rc is not None and lc is not None
    assert rc.get_value() == 45
    assert lc.get_value() == 18


def test_avl_correctly_remove_textbook():
    tree = build_avl_tree()
    for val in [16, 29, 18, 34, 26, 15, 45, 33, 6, 37, 49, 48, 40]:
        tree.insert(val)
    tree.remove(16)
    tree.remove(45)
    tree.remove(37)

    print(tree)
    root = tree.get_root()
    assert root is not None
    assert root.get_value() == 34
    assert root.balancing_factor() == -1
    assert root.get_height() == 4
    rc, lc = root.get_right_child(), root.get_left_child()
    assert rc is not None and lc is not None
    assert rc.get_value() == 48
    assert lc.get_value() == 18


def main():
    test_avl_single_right_rotation_ll_case()
    test_avl_single_left_rotation_rr_case()
    test_avl_left_right_rotation_lr_case()
    test_avl_right_left_rotation_rl_case()
    test_avl_no_rebalance_needed()
    test_avl_correctly_insert_textbook()
    test_avl_correctly_remove_textbook()
    return 0


if __name__ == "__main__":
    main()
