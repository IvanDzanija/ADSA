from Nodes import BinaryNode
from BinaryTree import BinaryTree


def main():
    # Create an empty tree
    tree = BinaryTree()

    # Insert nodes
    for value in [5, 3, 7, 2, 4, 6, 8]:
        tree.insert(value)

    # Pretty print the tree
    print("📦 Binary Tree Structure:")
    print(tree)
    print()

    # Test search
    print("🔍 Searching for value 4:")
    node = tree.binary_search(4)
    if node:
        print(f"Found node with value {node.get_value()}")
    else:
        print("Value not found.")
    print()

    print("🔍 Searching for value 9:")
    node = tree.binary_search(9)
    if node:
        print(f"Found node with value {node.get_value()}")
    else:
        print("Value not found.")
    print()

    # Find leftmost and rightmost nodes
    leftmost = tree.find_leftmost()
    rightmost = tree.find_rightmost()
    print(f"🌿 Leftmost node: {leftmost.get_value() if leftmost else 'None'}")
    print(f"🌿 Rightmost node: {rightmost.get_value() if rightmost else 'None'}")
    print()

    # Try inserting a duplicate
    print("➕ Trying to insert duplicate value 3:")
    tree.insert(3)
    print(tree)


if __name__ == "__main__":
    main()
