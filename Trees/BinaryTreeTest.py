import pytest
from BinaryTree import BinaryTree
from Nodes import BinaryNode


@pytest.fixture
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


# -------------------------------------------------------
# INSERTION TESTS
# -------------------------------------------------------
def test_insert_root():
    tree = BinaryTree()
    node = tree.insert(10)
    assert tree.root == node
    assert node is not None and node.get_value() == 10
    assert str(tree.root) == "10"


def test_insert_multiple_nodes(sample_tree):
    # Verify BST property and structure
    assert sample_tree.root.get_value() == 5
    assert sample_tree.root.get_left_child().get_value() == 3
    assert sample_tree.root.get_right_child().get_value() == 7
    assert sample_tree.root.get_left_child().get_left_child().get_value() == 2
    assert sample_tree.root.get_left_child().get_right_child().get_value() == 4
    assert sample_tree.root.get_right_child().get_left_child().get_value() == 6
    assert sample_tree.root.get_right_child().get_right_child().get_value() == 8


def test_insert_duplicate_value(capsys):
    tree = BinaryTree()
    tree.insert(5)
    duplicate = tree.insert(5)
    out, _ = capsys.readouterr()
    assert "already exist" in out
    assert duplicate is None


# -------------------------------------------------------
# SEARCH TESTS
# -------------------------------------------------------
def test_binary_search_found(sample_tree):
    node = sample_tree.binary_search(4)
    assert node is not None
    assert node.get_value() == 4


def test_binary_search_not_found(sample_tree):
    node = sample_tree.binary_search(100)
    assert node is None


# -------------------------------------------------------
# STRUCTURE TESTS
# -------------------------------------------------------
def test_pretty_print_output(sample_tree):
    output = str(sample_tree)
    # Ensure all values appear in the printed tree
    for val in ["2", "3", "4", "5", "6", "7", "8"]:
        assert val in output
    # Ensure root label is correct
    assert "Root:" in output


def test_subtree_node_count(sample_tree):
    assert sample_tree.root.get_subtree_nodes_count() == 7
    left = sample_tree.root.get_left_child()
    right = sample_tree.root.get_right_child()
    assert left.get_subtree_nodes_count() == 3
    assert right.get_subtree_nodes_count() == 3


# -------------------------------------------------------
# HEIGHT / BALANCE TESTS
# -------------------------------------------------------
def test_node_height_computation(sample_tree):
    # Leaf nodes should have height 0
    assert sample_tree.binary_search(2).get_height() == 0
    # Height of root should be 2 (levels: 5 → 3/7 → 2/4/6/8)
    assert sample_tree.root.get_height() == 2


def test_balancing_factor(sample_tree):
    root = sample_tree.root
    assert root.balancing_factor() == 0  # symmetrical tree
    left = root.get_left_child()
    assert left.balancing_factor() == 0


# -------------------------------------------------------
# DELETION TESTS
# -------------------------------------------------------
def test_remove_leaf(sample_tree):
    # Remove a leaf (8)
    sample_tree.remove(8)
    assert sample_tree.binary_search(8) is None
    output = str(sample_tree)
    assert "8" not in output


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
    assert tree.root.get_left_child().get_value() == 4


def test_remove_node_with_two_children(sample_tree):
    """
    Remove node 3 → has two children (2, 4)
    Should replace with its in-order predecessor (2 or 4)
    """
    sample_tree.remove(3)
    output = str(sample_tree)
    assert "3" not in output
    # Root should remain the same
    assert sample_tree.root.get_value() == 5
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


def test_remove_from_empty_tree(capsys):
    tree = BinaryTree()
    tree.remove(10)
    out, _ = capsys.readouterr()
    assert "Tree is empty" in out
