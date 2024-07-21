class Solution:
    @staticmethod
    def count_characters(input_string: str) -> dict[str, int]:
        """
        Count the occurrences of each character in the input string.

        Average and Worst Case Time Complexity:
        - O(N), where N is the length of the input string.

        Average and Worst Case Space Complexity:
        - O(N), where N is the number of unique characters in the input string.
        """
        count_dict: dict[str, int] = {}
        for char in input_string:
            count_dict[char] = count_dict.get(char, 0) + 1
        return count_dict

    def isAnagram(self, s: str, t: str) -> bool:
        """
        Strategy:
        1. Use a dictionary to count the occurrences of each character for s and t.
        2. Compare the two dictionaries by value.

        Average Time Complexity:
        - O(N + M), where N is the length of s and M is the length of t.
        - O(N) to count characters in s.
        - O(M) to count characters in t.
        - O(min(N, M)) to compare the two dictionaries.

        Worst Case Time Complexity:
        - O(N + M), where N is the length of s and M is the length of t.
        - Even in the worst case, the time complexity remains O(N + M) because the creation and comparison of dictionaries
          do not exceed linear time relative to the input size.

        Average Space Complexity:
        - O(N + M), where N is the number of unique characters in s and M is the number of unique characters in t.

        Worst Case Space Complexity:
        - O(N + M), where N is the number of unique characters in s and M is the number of unique characters in t.
        """
        s_count: dict[str, int] = self.count_characters(s)
        t_count: dict[str, int] = self.count_characters(t)
        # returns True if both dictionaries have the same keys and values
        return s_count == t_count
