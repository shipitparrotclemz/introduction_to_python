from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[int]:
        """
        Challenge 1:
        - Given a list of words:

        Input: words = ["Hello","Alaska","Dad","Peace"]

        Answer: [1, 1, 1, 0]

        Return the row which belongs to the first character
        """
        first_row: str = "QWERTYUIOP"
        second_row: str = "ASDFGHJKL"
        third_row: str = "ZXCVBNM"
        return []


if __name__ == "__main__":
    solution: Solution = Solution()
    words = ["Hello","Alaska","Dad","Peace"]
    answer: List[int] = solution.findWords(words)
    assert answer == [1, 1, 1, 0]