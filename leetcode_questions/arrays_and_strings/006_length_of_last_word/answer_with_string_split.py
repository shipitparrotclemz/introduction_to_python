class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Strategy: Split string into words, and get the length of the last word

        N is the number of characters in s

        Average and Worst Case Time Complexity: O(N)
        - O(N) to iterate the string and split the characters by whitespace.

        Average and Worst Case Space Complexity: O(N)
        - O(N) for storing the words in the list words.
        """
        words: list[str] = s.split()
        if not words:
            return 0
        last_word: str = words[-1]
        return len(last_word)
