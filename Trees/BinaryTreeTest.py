from BinaryTree import BinaryTree, BinaryNode


def sample_tree() -> BinaryTree:
    """
    Build the following binary search tree for testing:
                5
              /   \
             3     7
            / \\   / \\
           2  4  6   8
    """
    tree = BinaryTree()
    for value in [5, 3, 7, 2, 4, 6, 8]:
        tree.insert(value)
    return tree


tree = sample_tree()
# print(tree)


# -------------------------------------------------------
# INSERTION TESTS
# -------------------------------------------------------
def test_insert_root():
    tree = BinaryTree()
    node = tree.insert(10)
    assert node is not None and tree.root == node
    assert node.get_value() == 10
    assert str(tree.root) == "10"


def test_insert_multiple_nodes():
    # Verify property and structure
    assert tree.root is not None
    assert tree.root.get_value() == 5
    lc = tree.root.get_left_child()
    rc = tree.root.get_right_child()
    assert lc is not None and lc.get_value() == 3
    assert rc is not None and rc.get_value() == 7
    assert tree.root.get_left_child().get_left_child().get_value() == 2
    assert tree.root.get_left_child().get_right_child().get_value() == 4
    assert tree.root.get_right_child().get_left_child().get_value() == 6
    assert tree.root.get_right_child().get_right_child().get_value() == 8


def test_insert_duplicate_value():
    tree = BinaryTree()
    node = tree.insert(5)
    assert node is not None and node.get_value() == 5
    duplicate = tree.insert(5)
    assert duplicate is None


# -------------------------------------------------------
# SEARCH TESTS
# -------------------------------------------------------
def test_binary_search_found():
    node = tree.binary_search(4)
    assert node is not None
    assert node.get_value() == 4


def test_binary_search_not_found():
    node = tree.binary_search(100)
    assert node is None


# -------------------------------------------------------
# STRUCTURE TESTS
# -------------------------------------------------------
def test_pretty_print_output():
    output = str(tree)
    # Ensure all values appear in the printed tree
    for val in ["2", "3", "4", "5", "6", "7", "8"]:
        assert val in output
    # Ensure root label is correct
    assert "Root:" in output


def test_subtree_node_count():
    assert tree.root is not None
    assert tree.root.get_subtree_nodes_count() == 7
    left = tree.root.get_left_child()
    right = tree.root.get_right_child()
    assert left is not None and right is not None
    assert left.get_subtree_nodes_count() == 3
    assert right.get_subtree_nodes_count() == 3


# -------------------------------------------------------
# HEIGHT / BALANCE TESTS
# -------------------------------------------------------
def test_node_height_computation():
    # Leaf nodes should have height 0
    node = tree.binary_search(2)
    assert node is not None and node.get_height() == 1
    assert tree.root is not None and tree.root.get_height() == 3


def test_balancing_factor():
    root = tree.root
    assert root is not None and root.balancing_factor() == 0
    left = root.get_left_child()
    assert left is not None and left.balancing_factor() == 0


# -------------------------------------------------------
# DELETION TESTS
# -------------------------------------------------------
def test_remove_leaf():
    # Remove a leaf (8)
    tree.remove(8)
    assert tree.binary_search(8) is None


def test_remove_node_with_one_child():
    """
    Tree before:
          5
         /
        3
         \
          4
    Remove node 3 (has one right child)
    """
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(4)
    tree.remove(3)

    assert tree.binary_search(3) is None
    assert tree.binary_search(4) is not None
    assert tree.root is not None
    left = tree.root.get_left_child()
    assert left is not None and left.get_value() == 4


def test_remove_node_with_two_children():
    tree.remove(3)
    assert tree.binary_search(3) is None
    assert tree.binary_search(2) is not None
    assert tree.binary_search(4) is not None
    assert tree.root is not None and tree.root.get_value() == 5


def test_remove_root_with_two_children():
    tree.remove(5)
    assert tree.binary_search(5) is None
    assert tree.binary_search(2) is not None
    assert tree.binary_search(7) is not None
    assert tree.root is not None


def test_remove_from_empty_tree():
    tree = BinaryTree()
    tree.remove(10)


def test_balanced_tree_constructor():
    values = [1, 2, 3, 4, 5, 6, 7]
    tree = BinaryTree(values)
    assert tree.root is not None
    assert tree.root.get_value() == 4
    lc = tree.root.get_left_child()
    rc = tree.root.get_right_child()
    assert lc is not None and rc is not None
    assert lc.get_value() == 2
    assert rc.get_value() == 6
    for v in values:
        assert tree.binary_search(v) is not None


def test_find_leftmost_and_rightmost():
    tree = BinaryTree([1, 2, 3, 4, 5])
    root = tree.get_root()
    assert root is not None
    l = root.find_leftmost()
    assert l is not None and l.get_value() == 1
    r = root.find_rightmost()
    assert r is not None and r.get_value() == 5


def test_parent_child_relationships():
    tree = BinaryTree()
    n5 = tree.insert(5)
    n3 = tree.insert(3)
    n7 = tree.insert(7)
    assert n3.get_parent() == n5
    assert n7.get_parent() == n5
    assert n5.get_left_child() == n3
    assert n5.get_right_child() == n7


def test_rotate_right_single_rotation():
    tree = BinaryTree()
    n5 = tree.insert(5)
    n3 = tree.insert(3)
    n2 = tree.insert(2)
    n5.rotate_right(tree)

    root = tree.get_root()
    assert root.get_value() == 3
    assert root.get_left_child().get_value() == 2
    assert root.get_right_child().get_value() == 5


def test_rotate_left_single_rotation():
    tree = BinaryTree()
    n2 = tree.insert(2)
    n4 = tree.insert(4)
    n5 = tree.insert(5)
    n2.rotate_left(tree)

    root = tree.get_root()
    assert root.get_value() == 4
    assert root.get_left_child().get_value() == 2
    assert root.get_right_child().get_value() == 5


def test_balancing_factor_after_rotation():
    tree = BinaryTree()
    n5 = tree.insert(5)
    n3 = tree.insert(3)
    n2 = tree.insert(2)
    n5.rotate_right(tree)
    root = tree.get_root()
    assert root.balancing_factor() == 0


def test_make_root_and_set_parent():
    node = BinaryNode(10)
    parent = BinaryNode(5)
    node.set_parent(parent)
    assert node.get_parent() == parent
    node.make_root()
    assert node.get_parent() is None


def test_get_child_and_subtree_counts():
    tree = sample_tree()
    root = tree.get_root()
    assert root.get_child_count() == 2
    assert root.get_subtree_nodes_count() == 7
    leaf = tree.binary_search(2)
    assert leaf.get_child_count() == 0
    assert leaf.get_subtree_nodes_count() == 1


def test_balancing_factor_symmetry():
    tree = sample_tree()
    root = tree.get_root()
    bf_before = root.balancing_factor()
    tree.insert(9)
    bf_after = root.balancing_factor()
    assert bf_after >= bf_before


def test_make_right_backbone():
    tree = sample_tree()

    def make_right_backbone(tree):
        node = tree.root
        while node is not None:
            temp = node.get_left_child()
            if temp is not None:
                node.rotate_right(tree)
                node = temp
            else:
                node = node.get_right_child()

    make_right_backbone(tree)
    node = tree.get_root()
    while node:
        assert node.get_left_child() is None
        node = node.get_right_child()


def test_rotate_right_no_left_child_does_nothing():
    tree = BinaryTree()
    n5 = tree.insert(5)
    assert n5.rotate_right(tree) is None


def test_rotate_left_no_right_child_does_nothing():
    tree = BinaryTree()
    n5 = tree.insert(5)
    assert n5.rotate_left(tree) is None


def test_empty_tree_str():
    tree = BinaryTree()
    assert "(empty tree)" in str(tree)


def test_height_updates_correctly():
    tree = sample_tree()
    node = tree.binary_search(7)
    assert node is not None
    old_height = node.get_height()
    tree.insert(9)
    assert tree.binary_search(7).get_height() >= old_height


def main():
    test_insert_root()
    test_insert_multiple_nodes()
    test_insert_duplicate_value()
    test_binary_search_found()
    test_binary_search_not_found()
    test_pretty_print_output()
    test_subtree_node_count()
    test_node_height_computation()
    test_balancing_factor()
    test_remove_leaf()
    test_remove_node_with_one_child()
    test_remove_node_with_two_children()
    test_remove_root_with_two_children()
    test_remove_from_empty_tree()
    # New functionality tests
    test_balanced_tree_constructor()
    test_find_leftmost_and_rightmost()
    test_parent_child_relationships()
    test_rotate_right_single_rotation()
    test_rotate_left_single_rotation()
    test_balancing_factor_after_rotation()
    test_make_root_and_set_parent()
    test_get_child_and_subtree_counts()
    test_balancing_factor_symmetry()
    test_make_right_backbone()
    test_rotate_right_no_left_child_does_nothing()
    test_rotate_left_no_right_child_does_nothing()
    test_empty_tree_str()
    test_height_updates_correctly()


if __name__ == "__main__":
    main()
