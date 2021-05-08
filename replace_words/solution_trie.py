from typing import List


class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = Node()

    # `insert` follows formal Trie implementation
    def insert(self, word):
        node = self.root

        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            next_node = node.children[idx]

            # insert new Node
            if not next_node:
                node.children[idx] = Node()

            node = next_node

        # need to mark the end of the word
        node.isWord = True

    def get_shortest_prefix(self, word):
        node = self.root

        for i in range(len(word)):
            idx = ord(word[i]) - ord('a')
            next_node = node.children[idx]

            if not next_node:
                return word

            node = next_node

            # return shortest possible prefix
            if node.isWord:
                return word[:i + 1]

        return word


# 648. Replace Words
# Difficulty: Medium
# Time Complexity: O(N)
# explanation:
#   if the word doesn't match any root in dictionary then it would return immediately
#   or if it matches, it can possibly have maximum length of the length of the shortest root
#   so we can say that finding shortest prefix operation ends in constant time. O(1)
#   therefore we do constant time operation for every words such that overall time complexity becomes O(N)
#   where N is the length of the words in the sentence
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for root in dictionary:
            trie.insert(root)

        words = sentence.split(" ")
        return " ".join(trie.get_shortest_prefix(word) for word in words)

