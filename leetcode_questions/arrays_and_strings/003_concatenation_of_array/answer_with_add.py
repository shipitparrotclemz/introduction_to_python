from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Strategy:
        - Create a new list, which is a naive concatenation of the original list

        Given N as the number of items in the list

        Average + Worst Case Time Complexity: O(N)

        - O(2N) to create a new list with double the numbers in nums

        Average + Worst Case Space Complexity: O(N)

        - O(2N) to assign random access memory for storing the numbers in nums
        """
        return nums + nums