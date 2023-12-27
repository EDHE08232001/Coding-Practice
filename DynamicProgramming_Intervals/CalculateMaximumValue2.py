from typing import List

class CalculateMaximumValue2:
    def max_value(self, numStr: str) -> int:
        """
        Calculate the maximum value by inserting either '*' or '+' between the digits in the string.
        
        Args:
        numStr: A string of numbers (digits) for which we need to find the maximum value by insertion.

        Returns:
        The maximum value obtained by inserting either '*' or '+' between the digits of numStr.

        Time Complexity: O(n^3), where n is the length of numStr. This is due to the three nested loops:
                        one for the length of the substrings, one for the starting index of the substring,
                        and one for splitting the substring into two parts.
        """
        # Edge case: if the input string is empty, return -1 as an error indication.
        if not numStr:
            return -1
        
        # n is the length of the input string.
        n = len(numStr)
        
        # Initialize a 2D array dp where dp[i][j] represents the maximum value
        # for the substring numStr[i:j+1].
        dp = [[0] * n for _ in range(n)]

        # Base case: single digit values are the maximum for substrings of length 1.
        for i in range(n):
            dp[i][i] = int(numStr[i])
        
        # Consider all possible substrings of length 2 to n.
        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                # Calculate the maximum value for substring numStr[left:right+1]
                # by trying all possible positions (k) to split the substring
                # and applying either '*' or '+' operation.
                for k in range(left, right):
                    # compare inserting *, inserting +, and the current value, then choose the max value
                    dp[left][right] = max(dp[left][k] * dp[k + 1][right], dp[left][k] + dp[k + 1][right], dp[left][right])

        # The maximum value for the entire string is in dp[0][n - 1].
        return dp[0][n - 1]

# Example usage:
numStr = "123456"
obj = CalculateMaximumValue2()
print(obj.max_value(numStr))
