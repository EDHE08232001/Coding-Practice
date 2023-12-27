class WildcardMatching:
    def is_match(self, s: str, p: str) -> bool:
        """
        Determine if the string 's' matches the pattern 'p', where 'p' includes
        wildcard characters '?' (matches any single character) and '*' (matches any sequence of characters).

        Time Complexity: O(n*m), where n is the length of the string 's' and m is the length of the pattern 'p'.
        This is due to the nested loops traversing each character of the string and pattern.

        Space Complexity: O(n*m), for storing the DP table.

        :param s: The source string.
        :param p: The pattern string containing '?' and '*'.
        :return: True if 's' matches pattern 'p', False otherwise.

        Examples:
            is_match("aab", "c*a*b") -> False
            is_match("abc", "*?c") -> True
        """
        if s is None or p is None:
            return False

        n, m = len(s), len(p)

        # Initialize a DP table where dp[i][j] is True if the first i characters of 's'
        # match the first j characters of 'p'.
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # Base case: empty string matches with empty pattern.
        dp[0][0] = True

        # Base case for patterns with '*' only.
        for i in range(1, m + 1):
            dp[0][i] = dp[0][i - 1] and p[i - 1] == '*'

        # Populate the DP table.
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    # '*' can match zero characters (dp[i][j-1]) or one/more characters (dp[i-1][j]).
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    # Match if the current characters are the same or if the pattern has '?'
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')

        return dp[n][m]


# Example usage:
obj = WildcardMatching()
print(obj.is_match("abc", "*?c"))  # Output: True
