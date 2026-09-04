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


class MedianFinder:
    def __init__(self):
        pass

    def add_num(self, num: int) -> None:
        pass

    def find_median(self) -> float:
        pass


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
