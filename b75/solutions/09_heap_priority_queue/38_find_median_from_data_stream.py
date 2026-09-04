"""
Find Median from Data Stream
--------------------------------
The median is the middle value in an ordered integer list. If the size of
the list is even, the median is the average of the two middle values.

Implement the MedianFinder class:
    - MedianFinder() Initializes the object.
    - void addNum(int num) Adds `num` to the data structure.
    - double findMedian() Returns the median of all elements so far.

Example 1:
    Input:
        medianFinder = MedianFinder()
        medianFinder.addNum(1)
        medianFinder.addNum(2)
        medianFinder.findMedian() -> 1.5
        medianFinder.addNum(3)
        medianFinder.findMedian() -> 2.0

Constraints:
    -10^5 <= num <= 10^5
    At most 5 * 10^4 calls will be made to addNum and findMedian.
"""

import heapq


class MedianFinder:
    def __init__(self):
        # max-heap (store negated values) for the smaller half of the numbers
        self.small = []
        # min-heap for the larger half of the numbers
        self.large = []

    def add_num(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        # ensure every value in `small` <= every value in `large`
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # keep sizes balanced: len(small) == len(large) or len(small) == len(large) + 1
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


if __name__ == "__main__":
    median_finder = MedianFinder()
    steps = [
        ("add_num", 1, None),
        ("add_num", 2, None),
        ("find_median", None, 1.5),
        ("add_num", 3, None),
        ("find_median", None, 2.0),
    ]

    for op, arg, expected in steps:
        result = getattr(median_finder, op)(arg) if arg is not None else getattr(median_finder, op)()
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {op}({arg if arg is not None else ''}) = {result} (expected {expected})")
