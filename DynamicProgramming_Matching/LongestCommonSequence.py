class LongestCommonSequence:
    def longest_common_subsequence(self, a: str, b: str) -> int:
        """
        Calculate the length of the longest common subsequence (LCS) between two strings.
        
        The LCS is the longest sequence that can be derived from both strings by deleting some characters
        (possibly zero) without changing the order of the remaining characters.

        Time Complexity: O(n*m), where 'n' is the length of string 'a' and 'm' is the length of string 'b'.
        This is due to the double nested loop that iterates over all pairs of indices in 'a' and 'b'.

        Space Complexity: O(n*m), for storing the DP table of size 'n+1' by 'm+1'.

        :param a: The first string.
        :param b: The second string.
        :return: The length of the longest common subsequence between 'a' and 'b'.

        Examples:
            longest_common_subsequence("abcde", "ace") -> 3
            longest_common_subsequence("abc", "def") -> 0
        """
        # Base case: if either string is empty, the LCS is 0.
        if not a or not b:
            return 0

        n, m = len(a), len(b)

        # Initialize a DP table where dp[i][j] represents the length of LCS of the first i characters of 'a'
        # and the first j characters of 'b'.
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill the DP table.
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If characters match, take the diagonal value and add 1.
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # If characters don't match, take the maximum value from the left or top cell.
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        # The bottom-right cell contains the length of the LCS.
        return dp[n][m]


# Example usage:
lcs = LongestCommonSequence()
print(lcs.longest_common_subsequence("abcde", "ace"))  # Output: 3