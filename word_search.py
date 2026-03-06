"""
Word search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Approach: DFS backtrack
Time complexity: O(m*n)
Space complexity: O(1)


Problem:
Given an m×n board and a word, return true if the word exists in the grid
using horizontally or vertically adjacent cells. Each cell may only be used once.

Example:
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED" → True
word = "SEE" → True
word = "ABCB" → False

Approach:
DFS + backtracking from every cell. If current char matches word[depth],
mark cell visited (overwrite with '#'), recurse into 4 neighbors for next char.
Restore cell on backtrack. Prune early when char doesn't match.

def exist(board, word):
    for row in range(rows):
        for col in range(cols):
            if dfs(board, row, col, 0):
                return True
    return False

def dfs(board, row, col, depth):
    if depth == len(word): return True
    if row < 0 or row >= rows or col < 0 or col >= cols: return False
    if board[row][col] != word[depth]: return False
    board[row][col] = '#'                   # mark visited
    found = any(dfs(board, row + dr, col + dc, depth + 1)
                for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)])
    board[row][col] = word[depth]           # restore
    return found

Time: O(m × n × 4^L) where L = len(word)
Space: O(L) recursion stack depth

Triggers:
- find a single word in a grid
- path exists with no cell reuse
- DFS + backtrack with in-place visited marking

Variants / Watch-outs:
- Optimisation angle: early termination — if remaining board cells < remaining word
  chars needed, prune immediately (count available matching chars)
- Word Search II (multiple words): Trie + this DFS — shared prefix pruning replaces
  per-word separate DFS
- The '#' overwrite trick avoids a visited set entirely — restore ensures correctness
"""
from typing import List
from unittest import TestCase


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if self.dfs(board, row, col, word[1:]):
                        return True
        return False

    def dfs(self, board: List[List[str]], row: int, col: int, word: str) -> bool:
        # matched
        if not word:
            return True
        # mark the row, col visited
        temp_origin, board[row][col] = board[row][col], "#"
        rows, cols = len(board), len(board[0])
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for x, y in direction:
            new_row, new_col = x + row, y + col
            if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols and board[new_row][new_col] == word[
                0]:
                # already matched
                if self.dfs(board, new_row, new_col, word[1:]):
                    return True

        # get back the original start
        board[row][col] = temp_origin
        return False


class TestWordSearch(TestCase):
    def setUp(self) -> None:
        self.board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        self.board_1 = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]

    def test_word_search(self) -> None:
        obj = Solution()
        self.assertTrue(obj.exist(self.board, "ABCCED"))
        self.assertTrue(obj.exist(self.board, "ESE"))
        self.assertFalse(obj.exist(self.board, "ABCB"))
        self.assertTrue(obj.exist(self.board_1, "AAB"))
