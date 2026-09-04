"""
Implement Trie (Prefix Tree)
--------------------------------
A trie (pronounced as "try") or prefix tree is a tree data structure used
to efficiently store and retrieve keys in a dataset of strings.

Implement the Trie class:
    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string `word` into the trie.
    - boolean search(String word) Returns True if `word` is in the trie
      (i.e., was inserted before), and False otherwise.
    - boolean startsWith(String prefix) Returns True if there is a
      previously inserted string that has `prefix` as a prefix, and False
      otherwise.

Example 1:
    Input:
        trie = Trie()
        trie.insert("apple")
        trie.search("apple")   -> True
        trie.search("app")     -> False
        trie.startsWith("app") -> True
        trie.insert("app")
        trie.search("app")     -> True

Constraints:
    1 <= len(word), len(prefix) <= 2000
    word and prefix consist only of lowercase English letters.
    At most 3 * 10^4 calls in total will be made to insert, search, and
    startsWith.
"""


class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True

    def _find(self, word: str):
        node = self
        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        return self._find(prefix) is not None


if __name__ == "__main__":
    trie = Trie()
    steps = [
        ("insert", "apple", None),
        ("search", "apple", True),
        ("search", "app", False),
        ("starts_with", "app", True),
        ("insert", "app", None),
        ("search", "app", True),
    ]

    for op, arg, expected in steps:
        result = getattr(trie, op)(arg)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {op}({arg!r}) = {result} (expected {expected})")
