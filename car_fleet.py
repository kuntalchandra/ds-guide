"""
Car Fleet

N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the
target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also
a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?



Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.


O(NlogN) To sort the cars by position
O(N) One pass for all cars
O(N) Space for sorted cars. O(1) space is possible if we sort pos in-place.
"""
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position:
            return 0
        cars = []

        # Calculate the needed time
        for i in range(len(position)):
            distance = target - position[i]
            needed_time = distance / speed[i]
            cars.append([needed_time, position[i]])

        # Sort by position in desc order so that the closest one reaches first
        cars.sort(key=lambda n: n[1], reverse=True)
        fleet = 1
        arrival_time, _ = cars[0]

        # If arrival time is lesser, then consider it's a fleet
        for i in range(1, len(cars)):
            if cars[i][0] > arrival_time:
                fleet += 1
                arrival_time = cars[i][0]

        return fleet