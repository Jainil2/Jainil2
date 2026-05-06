class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:

    def countPrefixSuffixPairs(self, words):

        root = TrieNode()

        ans = 0

        for word in words:

            node = root
            n = len(word)

            for i in range(n):

                key = (word[i], word[n - 1 - i])

                if key not in node.children:
                    node.children[key] = TrieNode()

                node = node.children[key]

                ans += node.count

            node.count += 1

        return ans