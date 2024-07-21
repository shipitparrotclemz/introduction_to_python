class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Strategy: Iterate characters from right to left until we see white space

        N is the number of characters in s

        Average and Worst Case Time Complexity: O(N)
        - O(N) to iterate through the string

        Average and Worst Case Space Complexity: O(1)
        - Constant memory used for the index pointers
        """
        # Initialize variables to track the start and end of the last word
        detected_word: bool = False
        back_of_word_index: int = 0
        start_of_word_index: int = 0

        for index in range(len(s) - 1, -1, -1):
            if not detected_word and s[index] != " ":
                detected_word = True
                back_of_word_index = index
            if detected_word and s[index] == " ":
                start_of_word_index = index + 1
                break

        # If no word has been detected, handle edge cases where s is empty or has no words
        if not detected_word:
            return 0

        # Return the length of the last word
        return back_of_word_index - start_of_word_index + 1
