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

        # complete answer here
        return answer


if __name__ == "__main__":
    solution: Solution = Solution()
    words = ["Hello", "Alaska", "Dad", "Peace"]
    answer: List[str] = solution.findWords(words)
    assert answer == ["Alaska", "Dad"]
