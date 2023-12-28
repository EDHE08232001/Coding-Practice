class NumDecodings:
    def num_decodings(self, s: str) -> int:
        """
        Calculate the number of ways to decode a string of digits where 'A' to 'Z' 
        correspond to '1' to '26'.

        :param s: The input string representing encoded digits.
        :return: The total number of ways to decode the string.

        Time Complexity: O(n), where n is the length of the input string.
        """

        # Base case: if the input string is empty, there are no ways to decode it.
        if not s:
            return 0
        
        n = len(s)  # Length of the input string.

        # State: dp[i % 3] represents the number of ways to decode the first i characters.
        dp = [0, 0, 0]

        # Initialization: Setting up the base cases.
        dp[0] = 1  # An empty string has one way to be decoded.
        dp[1] = self.decode_ok(s[0])  # The first character's decodability.

        # Function: Iterate through the string, updating the state for each character.
        for i in range(2, n + 1):
            single = self.decode_ok(s[i - 1:i])  # Decoding the single character.
            double = self.decode_ok(s[i - 2:i])  # Decoding the double character.
            dp[i % 3] = dp[(i - 1) % 3] * single + dp[(i - 2) % 3] * double

        # Answer: The number of ways to decode the whole string.
        return dp[n % 3]

    def decode_ok(self, substr: str) -> int:
        """
        Check if a substring can represent a valid code (either a single digit or a pair of digits).

        :param substr: The substring to check.
        :return: 1 if the substring is a valid code, 0 otherwise.
        """
        # Convert the substring to an integer to check its validity.
        code = int(substr)

        # Check if the substring is a valid single-digit code.
        if len(substr) == 1 and 1 <= code <= 9:
            return 1

        # Check if the substring is a valid two-digit code.
        if len(substr) == 2 and 10 <= code <= 26:
            return 1

        return 0  # Return 0 if the substring does not represent a valid code.