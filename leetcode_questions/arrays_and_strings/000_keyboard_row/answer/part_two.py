from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        """
        Challenge 1:
        - Given a list of words:

        Input: words = ["Hello","Alaska","Dad","Peace"]

        Answer: ["Alaska", "Dad"]

        Return the words which can be formed with only one row on keyboard
        """
        first_row: str = "QWERTYUIOP"
        second_row: str = "ASDFGHJKL"
        third_row: str = "ZXCVBNM"
        answer: list[str] = []
        for word in words:
            # Get row word belongs to; based on first char
            first_char: str = word[0].upper()
            if first_char in first_row:
                row = first_row
            elif first_char in second_row:
                row = second_row
            else:
                row = third_row

            # Check 2nd and subsequent characters
            is_valid_word: bool = True
            for i in range(1, len(word)):
                # upper case before check; cos rows are upper cased
                curr_char = word[i].upper()
                if curr_char not in row:
                    is_valid_word = False
                    break

            if is_valid_word:
                answer.append(word)
        return answer


if __name__ == "__main__":
    solution: Solution = Solution()
    words = ["Hello", "Alaska", "Dad", "Peace"]
    answer: List[str] = solution.findWords(words)
    assert answer == ["Alaska", "Dad"], answer
