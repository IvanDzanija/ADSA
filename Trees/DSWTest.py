from DSW import DSW
from BinaryTree import BinaryTree
from math import ceil, log


def test_DSW_on_empty_tree():
    tree = BinaryTree()
    dsw = DSW(tree)
    dsw.DSW()
    assert tree.get_root() is None


def test_DSW_on_single_node_tree():
    tree = BinaryTree()
    tree.insert(10)
    dsw = DSW(tree)
    dsw.DSW()
    root = tree.get_root()
    assert root is not None
    assert root.get_value() == 10
    assert root.get_left_child() is None
    assert root.get_right_child() is None


def test_DSW_on_unbalanced_right_tree():
    """
    Build a skewed tree (like a linked list):
      1
       \\
        2
         \\
          3
           \\
            4
    """
    tree = BinaryTree()
    for v in [1, 2, 3, 4]:
        tree.insert(v)

    dsw = DSW(tree)
    dsw.DSW()

    root = tree.get_root()
    assert root is not None
    assert root.get_value() == 2
    height = root.get_height()
    assert height <= ceil(log(root.get_subtree_nodes_count() + 1, 2)) + 1


def test_DSW_on_left_heavy_tree():
    """
    Build a left-skewed tree:
           5
          /
         4
        /
       3
      /
     2
    After DSW -> should become balanced.
    """
    tree = BinaryTree()
    for v in [5, 4, 3, 2]:
        tree.insert(v)

    dsw = DSW(tree)
    dsw.DSW()

    root = tree.get_root()
    assert root is not None
    assert root.get_value() == 3
    left = root.get_left_child()
    right = root.get_right_child()
    assert (
        abs(
            (left.get_subtree_nodes_count() if left else 0)
            - (right.get_subtree_nodes_count() if right else 0)
        )
        <= 1
    )


def test_DSW_rotate_executes_without_error():
    tree = BinaryTree()
    for v in [1, 2, 3]:
        tree.insert(v)
    dsw = DSW(tree)
    dsw._DSW_rotate(1)
    assert tree.get_root() is not None


def test_DSW_reduces_tree_height():
    tree = BinaryTree()
    for v in [1, 2, 3, 4, 5, 6, 7]:
        tree.insert(v)
    # print(tree)
    root_before = tree.get_root()
    assert root_before is not None
    height_before = root_before.get_height()

    dsw = DSW(tree)
    dsw.DSW()

    root_after = tree.get_root()
    assert root_after is not None
    height_after = root_after.get_height()
    assert height_after < height_before
    print(tree)
    print(root_before, root_after, height_before, height_after)


def test_DSW_preserves_inorder_sequence():
    """
    DSW should not change the inorder traversal sequence (sorted order).
    """
    values = [1, 2, 3, 4, 5, 6, 7]
    tree = BinaryTree()
    for v in values:
        tree.insert(v)

    def inorder(node):
        return (
            inorder(node.get_left_child())
            + [node.get_value()]
            + inorder(node.get_right_child())
            if node
            else []
        )

    before = inorder(tree.get_root())

    dsw = DSW(tree)
    dsw.DSW()

    after = inorder(tree.get_root())

    assert before == after  # inorder traversal preserved


def test_DSW_on_perfect_tree_does_nothing():
    """
    If the tree is already balanced, DSW should not change it significantly.
    """
    tree = BinaryTree([1, 2, 3, 4, 5, 6, 7])
    dsw = DSW(tree)
    before_root_value = tree.get_root().get_value()
    before_height = tree.get_root().get_height()

    dsw.DSW()

    after_root_value = tree.get_root().get_value()
    after_height = tree.get_root().get_height()
    assert abs(before_height - after_height) <= 1
    assert before_root_value == after_root_value


def main():
    test_DSW_on_empty_tree()
    test_DSW_on_single_node_tree()
    test_DSW_on_unbalanced_right_tree()
    test_DSW_on_left_heavy_tree()
    test_DSW_rotate_executes_without_error()
    test_DSW_reduces_tree_height()


if __name__ == "__main__":
    main()
