from __future__ import annotations


class TrieNode:
    children: list[TrieNode | None] = [None] * 256
    child_count = 0

    def __init__(self, parent=None):
        self.parent = parent

    def is_leaf(self):
        return self.child_count == 0

    def transition(self, value: str) -> TrieNode | None:
        return self.children[ord(value)]

    def insert(self, value: str):
        node = self.transition(value)
        if node is None:
            new_node = TrieNode(self)
            self.children[ord(value)] = new_node
            self.child_count += 1
            return new_node
        return node
