from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Strategy:
        1. Use a set to store seen numbers, and check if a number has been seen before in O(1) average time complexity.
        2. Iterate through all numbers in the list. If a number has not been seen before, add it to the set;
           otherwise, return True.
        3. If the loop completes without finding duplicates, return False.

        Given N as the number of items in the list:

        Average Time Complexity: O(N)
        - The time taken to run scales linearly with N.
        - O(N) to iterate through all numbers.
        - At each step, O(1) time complexity to check if a number exists in the set or to add a number to the set.

        Average Space Complexity: O(N)
        - The space used scales linearly with N.
        - O(N) to store all numbers in the set.

        (Optional Detail): Worst-case runtime scenario happens when there are many hash collisions, though this is rare.
        - O(N) to iterate through all numbers.
        - At each step, O(N) worst-case time complexity to check or place an item in the set.
        - This results in an O(N^2) worst-case time complexity.

        Worst Case Space Complexity: O(N)
        - The space used scales linearly with N.
        - O(N) to store all numbers in the set.

        (Optional Detail): Best-case scenario happens when there are two identical numbers at the start of the list.
        - O(1) for early termination.
        """
        appeared: set[int] = set()
        for num in nums:
            if num in appeared:
                return True
            else:
                appeared.add(num)
        return False
