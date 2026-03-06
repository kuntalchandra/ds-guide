"""
Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation
sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

Approach:

    		      hit
		   /      |      \
		   *it   h*t   hi*
		 /|\     /|\     /|\

wordList = ["hot","dot","dog","lot","log","cog"]
change_map ={ *ot : hot, dot, lot
			h*t : hot
			ho* :hot
			d*t : dot
			do* : dot, dog
			*og : dog, log, cog
			d*g : dog
			l*t : lot
			lo* : lot, log
			l*g : log
			c*g: cog
			co* : cog
			}

			                            hit, level = 1
								 /            |              \
					     *it                h*t                  hi*
						   |                 |                     |
			             null  	       hot ,level = 2      null
										 /   |   \
										/    |     \
				               *ot           h*t      ho*
				           /    |   \         |        |
                     hot,2   dot,3  lot,3   hot,2    hot,2

Time complexity: O(num of words in the word list * length of words). In the worst case, need to traverse all the words
in word list * each word has length of changed words


Approach:
BFS for shortest path. Key optimisation: instead of comparing every word to every
other word O(n² × L), build a pattern map: each word generates L patterns
(replace each char with '*'). Words sharing a pattern are one transformation apart.
BFS level by level; level count = transformation steps.

# Build adjacency via patterns
pattern_map = defaultdict(list)
for word in word_list:
    for idx in range(len(word)):
        pattern = word[:idx] + '*' + word[idx+1:]
        pattern_map[pattern].append(word)

queue = deque([(begin_word, 1)])
visited = {begin_word}

while queue:
    word, distance = queue.popleft()
    for idx in range(len(word)):
        pattern = word[:idx] + '*' + word[idx+1:]
        for neighbour in pattern_map[pattern]:
            if neighbour == end_word: return distance + 1
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, distance + 1))
return 0

Time: O(n × L²) where n = words, L = word length
Space: O(n × L) for pattern map

Triggers:
- shortest path in an implicit graph
- transform one state to another in minimum steps
- BFS when all edges have equal weight (each step = 1)

Variants / Watch-outs:
- Optimisation angle: current repo solution is O(n × 26 × L) per node —
  pattern map pre-processing reduces repeated work significantly at scale
- Bidirectional BFS: expand from both ends simultaneously, O(b^(d/2)) vs O(b^d) —
  huge win when word list is large
"""
from collections import deque
from typing import List
from unittest import TestCase


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append((beginWord, 1))
        visited = set()
        word_list = set(wordList)

        while q:
            word, distance = q.popleft()
            if word == endWord:
                return distance
            for i in range(len(word)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    p_word = word[:i] + j + word[i + 1 :]
                    if p_word not in visited and p_word in word_list:
                        q.append((p_word, distance + 1))
                        visited.add(p_word)
        return 0


class TestLadderLength(TestCase):
    def setUp(self) -> None:
        self.b_word_1 = "hit"
        self.e_word_1 = "cog"
        self.w_list_1 = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.w_list_2 = ["hot", "dot", "dog", "lot", "log"]
        self.b_word_2 = "kiss"
        self.e_word_2 = "tusk"
        self.w_list_3 = [
            "miss",
            "dusk",
            "kiss",
            "musk",
            "tusk",
            "diss",
            "disk",
            "sang",
            "ties",
            "muss",
        ]

    def test_ladder_length(self) -> None:
        obj = Solution()
        self.assertEqual(
            5, obj.ladderLength(self.b_word_1, self.e_word_1, self.w_list_1)
        )
        self.assertEqual(
            0, obj.ladderLength(self.b_word_1, self.e_word_1, self.w_list_2)
        )
        self.assertEqual(
            5, obj.ladderLength(self.b_word_2, self.e_word_2, self.w_list_3)
        )
