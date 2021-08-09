"""
Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append([beginWord, 1])
        word_set = set(wordList)
        visited = set()

        while q:
            word, distance = q.popleft()
            if word == endWord:
                return distance
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    pos_word = word[:i] + char + word[i + 1:]
                    if pos_word in word_set and pos_word not in visited:
                        q.append([pos_word, distance + 1])
                        visited.add(pos_word)
        return 0