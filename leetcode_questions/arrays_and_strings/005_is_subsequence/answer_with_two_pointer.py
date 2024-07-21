class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Strategy: Two-pointer strategy

        - Use two pointers, one for s and one for t.
        - Initialize both pointers to the start of their respective strings.
        - Iterate through t, and check if the current character in t matches the current character in s.
        - If they match, move both pointers to the right.
        - If they don't match, move only the pointer for t to the right.
        - Continue this until either pointer reaches the end of its string.

        If the pointer for s reaches the end of s, all characters in s were found in t in order.

        Given N is the length of s and M is the length of t:

        Average and Worst Case Time Complexity: O(N + M)
        - O(N) to iterate through s.
        - O(M) to iterate through t.

        Average and Worst Case Space Complexity: O(1)
        - We only use two integer variables, which uses constant memory.
        """
        s_index: int = 0
        t_index: int = 0

        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1

        return s_index == len(s)
