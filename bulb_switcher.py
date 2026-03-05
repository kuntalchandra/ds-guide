"""
Bulb Switcher I
There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round,
you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

Approach:
There is a pattern for it
for 1th bulb : 1
2nd : 1 0
3rd : 1 0 0
4th : 1 0 0 1
5th : 1 0 0 1 0
6th : 1 0 0 1 0 0
7th : 1 0 0 1 0 0 0
8th : 1 0 0 1 0 0 0 0
9th : 1 0 0 1 0 0 0 0 1

Meaning the I-th bulb that is on only on when its on I**2 turn, for example if you want 2 bulb on then you will have to
go to 4th round, 3 bulb on -> 9th round.
so for (n-th round) you can get at most floor(square_root(n)) bulb.
https://leetcode.com/problems/bulb-switcher/discuss/383285/Python-99-One-line-solution-(its-math)

Bulb Switcher III

There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to right. Initially, all the bulbs are
turned off.

At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb change color to blue only if it is on and all
the previous bulbs (to the left) are turned on too.

Return the number of moments in which all turned on bulbs are blue.


Approach:
Bulb i gets toggled once for each divisor of i. It ends ON iff toggled an odd number of times.
Only perfect squares have an odd divisor count (the square root pairs with itself, not with another).
So the answer is simply floor(sqrt(n)).

return int(n ** 0.5)

Triggers:
- toggling across a range with divisor-based patterns
- "how many end in state X after n rounds"
- math insight replaces O(n²) simulation

Variants / Watch-outs:
- Never simulate — it's O(n²). The entire problem IS the math insight.
- Bulb Switcher II (with multiple operations): bitmask on first 6 bulbs (pattern repeats with period 6)
"""
from math import floor, sqrt
from typing import List


class Solution:
    def bulbSwitch(self, n: int) -> int:
        return floor(sqrt(n))

    def numTimesAllBlue(self, light: List[int]) -> int:
        right, res = 0, 0

        for idx, l in enumerate(light, 1):  # 2, 1, 3, 5, 4
            right = max(right, l)  # 2, 3, 5
            if right == idx:
                res += 1  # 1, 2, 3
        return res
