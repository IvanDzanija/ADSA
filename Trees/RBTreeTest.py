from RBTree import RBTree
from BinaryTree import BinaryNode


def sample_rbtree() -> RBTree:
    """
    Build a sample Red-Black Tree by inserting:
                5(B)
              /     \\
           3(B)     7(B)
          /   \\     /   \\
        2(R)  4(R) 6(R) 8(R)
    (Color assignments may vary slightly depending on balancing)
    """
    tree = RBTree()
    for value in [5, 3, 7, 2, 4, 6, 8]:
        tree.insert(value)
    return tree


# -------------------------------------------------------
# INSERTION TESTS
# -------------------------------------------------------
def test_insert_root_color():
    tree = RBTree()
    tree.insert(10)
    root = tree.get_root()
    assert root is not None
    assert root.get_value() == 10
    assert root.get_color() == "black"


def test_insert_red_child():
    tree = RBTree()
    tree.insert(10)
    tree.insert(5)
    root = tree.get_root()
    assert root is not None
    child = root.get_left_child()
    assert child is not None and child.get_color() == "red"
    assert root.get_color() == "black"


def test_insert_multiple_nodes_balanced():
    tree = RBTree()
    for v in [10, 5, 15, 3, 7, 13, 17]:
        tree.insert(v)
    root = tree.get_root()
    assert root is not None and root.get_color() == "black"
    assert all(n.get_color() in ["red", "black"] for n in tree.inorder_nodes()), (
        "All nodes must be properly colored"
    )


def test_no_two_red_nodes_in_a_row():
    tree = sample_rbtree()

    def check_no_double_red(node):
        if node is None:
            return True
        left = node.get_left_child()
        right = node.get_right_child()
        if node.get_color() == "red":
            if (left and left.get_color() == "red") or (
                right and right.get_color() == "red"
            ):
                return False
        return check_no_double_red(left) and check_no_double_red(right)

    assert check_no_double_red(tree.get_root()), "No red node should have a red child"


def test_all_paths_have_same_black_count():
    tree = sample_rbtree()

    def count_black_paths(node, black_count=0, results=None):
        if results is None:
            results = []
        if node is None:
            results.append(black_count + 1)  # NIL leaf counts as black
            return results
        if node.get_color() == "black":
            black_count += 1
        count_black_paths(node.get_left_child(), black_count, results)
        count_black_paths(node.get_right_child(), black_count, results)
        return results

    counts = count_black_paths(tree.get_root())
    assert len(set(counts)) == 1, f"Black heights differ: {counts}"


def test_root_always_black_after_insertions():
    tree = RBTree()
    for v in [10, 5, 15, 3, 7, 13, 17]:
        tree.insert(v)
        root = tree.get_root()
        assert root is not None and root.get_color() == "black"


# -------------------------------------------------------
# STRUCTURE TESTS
# -------------------------------------------------------
def test_insert_and_structure_integrity():
    tree = RBTree()
    for v in [5, 3, 7, 2, 4, 6, 8]:
        tree.insert(v)
    root = tree.get_root()
    assert root is not None
    assert root.get_value() == 5
    assert root.get_left_child() is not None
    assert root.get_right_child() is not None


# -------------------------------------------------------
# ROTATION & BALANCING TESTS
# -------------------------------------------------------
def test_balancing_after_left_rotation():
    # RR case
    tree = RBTree()
    for v in [10, 15, 20]:
        tree.insert(v)
    root = tree.get_root()
    assert root is not None and root.get_value() == 15
    assert root.get_color() == "black"


def test_balancing_after_right_rotation():
    ## LL case
    tree = RBTree()
    for v in [10, 5, 2]:
        tree.insert(v)
    root = tree.get_root()
    assert root is not None
    assert root.get_value() == 5
    assert root.get_color() == "black"


def test_balancing_after_zigzag_rotation():
    ## LR case
    tree = RBTree()
    for v in [10, 5, 7]:
        tree.insert(v)
    root = tree.get_root()
    assert root is not None
    assert root.get_value() == 7
    assert root.get_color() == "black"


def test_uncle_red_case():
    tree = RBTree()
    for v in [10, 5, 15, 3, 7, 13, 17]:
        tree.insert(v)
    root = tree.get_root()
    assert root is not None and root.get_color() == "black"
    assert not any(
        n.get_color() == "red"
        and (
            (n.get_left_child() and n.get_left_child().get_color() == "red")
            or (n.get_right_child() and n.get_right_child().get_color() == "red")
        )
        for n in tree.inorder_nodes()
    )


def test_node_color_set_and_get():
    node = BinaryNode(10)
    node.set_color("red")
    assert node.get_color() == "red"
    node.set_color("black")
    assert node.get_color() == "black"


def test_black_height_increases_correctly():
    tree = RBTree()
    tree.insert(10)
    root = tree.get_root()
    assert root is not None and root.get_color() == "black"
    old_height = root.get_height()
    tree.insert(5)
    root = tree.get_root()
    assert root is not None
    new_height = root.get_height()
    assert new_height >= old_height


def textbook_example_test():
    tree = RBTree()
    values = [16, 29, 18, 34, 26, 15, 45, 33, 6, 37, 49, 48, 40]
    for v in values:
        tree.insert(v)
        print(tree, "\n\n")


def main():
    test_insert_root_color()
    test_insert_red_child()
    test_insert_multiple_nodes_balanced()
    test_no_two_red_nodes_in_a_row()
    test_all_paths_have_same_black_count()
    test_root_always_black_after_insertions()
    test_insert_and_structure_integrity()
    test_balancing_after_left_rotation()
    test_balancing_after_right_rotation()
    test_balancing_after_zigzag_rotation()
    test_uncle_red_case()
    test_node_color_set_and_get()
    test_black_height_increases_correctly()
    textbook_example_test()


if __name__ == "__main__":
    main()
