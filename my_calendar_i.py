"""
Calendar booking I

Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double
booking.
Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open
interval [start, end), the range of real numbers x such that start <= x < end.
A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to
both events.)
For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully
without causing a double booking. Otherwise, return false and do not add the event to the calendar.
Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
Follow up: How to optimise the time complexity?
# TODO: Implement the binary approach


Approach:
Current solution is O(n) per booking (linear scan).
The optimised approach is a sorted list + binary search.
Use bisect to find where the new interval would sit among existing start times,
then only check its immediate neighbours for overlap.

import bisect
self.starts = []
self.ends = []

def book(start, end):
    idx = bisect.bisect_left(self.starts, start)
    # check right neighbour: does new interval overlap next booking?
    if idx < len(self.starts) and end > self.starts[idx]:
        return False
    # check left neighbour: does previous booking overlap new interval?
    if idx > 0 and self.ends[idx - 1] > start:
        return False
    self.starts.insert(idx, start)
    self.ends.insert(idx, end)
    return True

Time: O(n) per booking (insert into list is O(n) shift) → O(log n) with balanced BST
Space: O(n)

Triggers:
- online booking — each event arrives one at a time
- overlap check on insertion
- "can I add this interval without conflict"

Variants / Watch-outs:
- Optimisation angle: current O(n²) total — the TODO in the file is the real interview question:
  binary search reduces per-booking check to O(log n); fully optimal is a balanced BST (SortedList from sortedcontainers)
- My Calendar II: track overlaps list separately; new booking fails only if it hits the
  overlaps list (triple booking), not the main calendar
"""


class MyCalendar:
    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        """
        Time complexity: O(n) to check n elements which leads to overall O(n^2)
        Space complexity: O(n)
        """
        for c_start, c_end in self.bookings:
            if start < c_end and end > c_start:
                return False
        self.bookings.append([start, end])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
