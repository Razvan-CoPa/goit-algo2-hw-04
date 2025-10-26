from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise TypeError("Input must be a list of strings")

        if not strings:
            return ""

        # Build Trie from all words
        for word in strings:
            self.put(word)

        prefix = ""
        node = self.root

        # Walk down the tree while there’s exactly one child and not an endpoint
        while len(node.children) == 1 and not node.is_end:
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]

        return prefix
