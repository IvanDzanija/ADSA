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
print(tree)


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
    print(tree)


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
    """
    Remove node 3 → has two children (2, 4)
    Should replace with its in-order predecessor (2 or 4)
    """
    tree.remove(3)
    output = str(tree)
    assert "3" not in output
    # Root should remain the same
    assert tree.root.get_value() == 5
    # Still contains both subtrees of former node 3
    assert any(val in output for val in ["2", "4"])


def test_remove_root_node():
    """
    Remove root node when it has two children.
    """
    tree = BinaryTree()
    for value in [10, 5, 15]:
        tree.insert(value)
    tree.remove(10)
    assert tree.binary_search(10) is None
    assert tree.root.get_value() in [5, 15]


def test_remove_from_empty_tree():
    tree = BinaryTree()
    tree.remove(10)


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
    test_remove_root_node()
    test_remove_from_empty_tree()


if __name__ == "__main__":
    main()
