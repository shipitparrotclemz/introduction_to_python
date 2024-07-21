from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Correct, but Time Limit Exceeded

        PS: Clement will crucify you if you do this

        Strategy: Naive Brute Force Solution

        Iterate from index 0 to the second last item:
        - For each element, iterate through all elements to its right to get the max value to its right

        Replace the last element with -1

        Given N as the number of items in arr

        Average and Worst Case Time Complexity: O(N^2)
        - O(N) to iterate from index 0 to the second last item.
        - For each iteration, O(N) to iterate through the remaining elements to the right.

        Average and Worst Case Space Complexity: O(1)
        - We modify the current arr in-place and do not use any additional space proportional to the input size.
        """
        # iterate from the first number to the second last number
        for index in range(0, len(arr) - 1):
            # get the greatest element to the right of the current number
            greatest_element_to_right: int = arr[index + 1]
            for right_index in range(index + 2, len(arr)):
                greatest_element_to_right = max(greatest_element_to_right, arr[right_index])
            # assign the current element with the greatest element among elements to its right
            arr[index] = greatest_element_to_right
        # replace the last element with -1
        arr[-1] = -1
        return arr
