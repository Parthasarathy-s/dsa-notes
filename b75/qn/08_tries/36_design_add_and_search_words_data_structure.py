"""
Design Add and Search Words Data Structure
------------------------------------------------
Design a data structure that supports adding new words and finding if a
string matches any previously added string.

Implement the WordDictionary class:
    - WordDictionary() Initializes the object.
    - void addWord(word) Adds `word` to the data structure.
    - bool search(word) Returns True if there is any string in the data
      structure that matches `word` or False otherwise. `word` may
      contain dots '.' where dots can be matched with any letter.

Example 1:
    Input:
        wordDictionary = WordDictionary()
        wordDictionary.addWord("bad")
        wordDictionary.addWord("dad")
        wordDictionary.addWord("mad")
        wordDictionary.search("pad") -> False
        wordDictionary.search("bad") -> True
        wordDictionary.search(".ad") -> True
        wordDictionary.search("b..") -> True

Constraints:
    1 <= len(word) <= 25
    word in addWord consists of lowercase English letters.
    word in search consists of '.' or lowercase English letters.
    At most 2 dots are allowed in the word for search queries.
    At most 10^4 calls will be made to addWord and search.
"""


class WordDictionary:
    def __init__(self):
        pass

    def add_word(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass


if __name__ == "__main__":
    word_dictionary = WordDictionary()
    steps = [
        ("add_word", "bad", None),
        ("add_word", "dad", None),
        ("add_word", "mad", None),
        ("search", "pad", False),
        ("search", "bad", True),
        ("search", ".ad", True),
        ("search", "b..", True),
    ]

    for op, arg, expected in steps:
        result = getattr(word_dictionary, op)(arg)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {op}({arg!r}) = {result} (expected {expected})")
