class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.value = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.words = []  # to make suffix counting easier

    def put(self, word: str, value=None):
        if not isinstance(word, str):
            raise TypeError("Word must be a string")
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.value = value
        self.words.append(word)  # store words for suffix lookup

    def get(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.value if node.is_end else None
