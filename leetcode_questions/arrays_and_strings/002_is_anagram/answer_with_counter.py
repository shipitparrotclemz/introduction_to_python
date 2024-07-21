from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Strategy:
        1. Use a Counter to count the occurrences of each character for s and t.
        2. Compare the two Counters by value.

        Given
        - N is the number of characters in s
        - M is the number of characters in t

        Average Time Complexity:
        - O(N + M)

        - O(N) to iterate each character in s to create the Counter.
        - O(M) to iterate each character in t to create the Counter.

        - O(min(N, M)) to compare the two Counters.

        Worst Case Time Complexity:
        - O(N + M)

        - Even in the worst case, the time complexity remains O(N + M) because the creation and comparison of Counters
          do not exceed linear time relative to the input size.
        """
        s_count: Counter = Counter(s)
        t_count: Counter = Counter(t)
        # returns True if both Counters have the same keys and values
        return s_count == t_count
