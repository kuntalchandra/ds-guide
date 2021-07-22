"""
Word Search II

 - Similar to Boggle
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word.
Example:
Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Trie + DFS
"""
from typing import List
from unittest import TestCase


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
        curr.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie_node = Trie()
        [trie_node.insert(word) for word in words]
        res = []
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                self.dfs(board, "", row, col, res, trie_node.root)
        return res

    def dfs(self, board: List[List[str]], word: str, row: int, col: int, res: List[str], trie_root: TrieNode):
        # It's a match
        if trie_root.is_word:
            res.append(word)
            trie_root.is_word = False

        char = board[row][col]
        # doesn't exist
        if char not in trie_root.children:
            return res

        board[row][col] = "#"
        node = trie_root.children[char]
        rows, cols = len(board), len(board[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for x, y in direction:
            new_row, new_col = row + x, col + y
            if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols:
                self.dfs(board, word + char, new_row, new_col, res, node)
        board[row][col] = char
        return res


class TestWordSearch(TestCase):
    def setUp(self) -> None:
        pass

    def test_word_search(self) -> None:
        obj = Solution()
        self.assertListEqual(
            ["eat", "oath"],
            sorted(
                obj.findWords(
                    [
                        ["o", "a", "a", "n"],
                        ["e", "t", "a", "e"],
                        ["i", "h", "k", "r"],
                        ["i", "f", "l", "v"],
                    ],
                    ["oath", "pea", "eat", "rain"],
                )
            ),
        )
