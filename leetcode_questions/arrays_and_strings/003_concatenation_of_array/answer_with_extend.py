from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Strategy:
        - Extend the original list `nums` by concatenating it with itself.

        This approach modifies the original list in place.

        Given N as the number of items in the list:

        Average and Worst Case Time Complexity: O(N)
        - O(N) to extend the list with its own elements.

        Average and Worst Case Space Complexity: O(N)
        - No additional space for a new list, but the existing list's size is doubled.

        PS: Modifying the list in production is not recommended.
        - Making a copy instead prevents subtle bugs where two or more places in the code base share the same mutable variable.
        """
        nums.extend(nums)
        return nums
