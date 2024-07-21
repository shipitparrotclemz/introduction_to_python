from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Strategy: Dynamic Programming; Re-use solution to the right

        Given a list [3,2,1]

        The smaller solution of max number to the right of 2 = 1
        Can be re-used to get the larger solution of max number to the right of 3 = 2

        By getting the max number to the right of a number, from right to left
        We avoid unnecessary scanning of numbers again.

        Iterate from the second last item to the first number:
        - For each element, the answer for the right element represents the largest number of all numbers to the right of it.
        - The largest number of the number is then the answer for the position to its right, and its number.

        Remember to store the number before overriding it.
        We replace the number before using the number to calculate the answer for the next iteration. Storing this number in a temporary variable prevents this.

        Replace the last element with -1.

        Given N as the number of items in arr:

        Average and Worst Case Time Complexity: O(N)
        - O(N) to iterate from the second last item to the first.
        - For each iteration, O(1) to calculate the max of two numbers to the right.

        Average and Worst Case Space Complexity: O(1)
        - We modify the current arr in-place and do not use any additional space proportional to the input size.
        """
        # Store the last element before overwriting it
        prev_number: int = arr[-1]
        # Replace the last element with -1
        arr[-1] = -1

        # Iterate from the second last number to the first element
        for index in range(len(arr) - 2, -1, -1):
            # Calculate the greatest element to the right of the current number
            greatest_element_to_right: int = max(prev_number, arr[index + 1])
            # Store the current number before overwriting
            prev_number = arr[index]
            # Update the current number with the greatest element to the right
            arr[index] = greatest_element_to_right

        return arr
