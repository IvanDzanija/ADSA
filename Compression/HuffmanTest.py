from Huffman import Huffman


def build_huffman():
    return Huffman()


def test_huffman_basic_round_trip():
    """
    Tests that we can encode a string and decode it back to the original.
    """
    h = build_huffman()
    original_text = "banana"

    # This will trigger _build_from_raw internally
    encoded = h.encode(original_text)
    decoded = h.decode(encoded)

    assert encoded != original_text
    # "banana": b(1), a(3), n(2). 'a' should be shortest code.
    # Possible codes: a:0, n:10, b:11 (lengths may vary depending on sort stability, but 'a' must be shortest or equal shortest)
    assert all(c in ["0", "1"] for c in encoded)
    assert decoded == original_text


def test_huffman_manual_build():
    """
    Tests building the tree with explicit probabilities.
    Symbols: A: 5, B: 9, C: 12, D: 13, E: 16, F: 45
    This is a classic textbook example.
    """
    h = build_huffman()
    symbols = ["A", "B", "C", "D", "E", "F"]
    freqs = [5, 9, 12, 13, 16, 45]

    # Input MUST be sorted by frequency for the deque implementation to work
    h.build(symbols, freqs)

    # Check properties of the resulting tree
    # F (45) is very frequent, should have a short code (likely 1 bit, e.g., '0')
    # A (5) is rare, should have a long code (e.g., 4 bits, '1100')

    code_f = h.coding_table["F"]
    code_a = h.coding_table["A"]

    assert len(code_f) < len(code_a)
    assert len(code_f) == 1
    assert len(code_a) >= 3


def test_huffman_single_character_edge_case():
    """
    Edge case: String contains only one type of character.
    Standard Huffman might fail to generate path of length > 0 without adjustment.
    """
    h = build_huffman()
    text = "aaaaa"
    encoded = h.encode(text)
    decoded = h.decode(encoded)

    # Should still work round trip
    assert decoded == "aaaaa"
    # Should produce actual bits (not empty string)
    assert len(encoded) > 0


def test_huffman_empty_string():
    """
    Edge case: Empty input.
    """
    h = build_huffman()
    assert h.encode("") == ""
    assert h.decode("") == ""


def test_huffman_textbook_mississippi():
    """
    Test with 'mississippi'.
    freqs: i:4, s:4, p:2, m:1
    """
    h = build_huffman()
    text = "mississippi"
    h.encode(text)

    table = h.coding_table
    # 'm' and 'p' are least frequent, should have longest codes
    # 'i' and 's' are most frequent, should have shortest codes

    assert len(table["i"]) <= len(table["p"])
    assert len(table["s"]) <= len(table["m"])

    # Verify prefix property (no code is prefix of another)
    codes = list(table.values())
    for i in range(len(codes)):
        for j in range(len(codes)):
            if i != j:
                assert not codes[i].startswith(codes[j])


def main():
    test_huffman_basic_round_trip()
    test_huffman_manual_build()
    test_huffman_single_character_edge_case()
    test_huffman_empty_string()
    test_huffman_textbook_mississippi()
    print("All Huffman tests passed.")


if __name__ == "__main__":
    main()
