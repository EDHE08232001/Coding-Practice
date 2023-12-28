class WordBreak:
    def word_break(self, s: str, word_set: set) -> bool:
        """
        Determines if the string can be segmented into a space-separated sequence of one or more dictionary words.

        :param s: The string to be segmented.
        :param word_set: The set containing all the words.
        :return: True if the string can be segmented, False otherwise.

        Time Complexity: O(n^2 * m), where n is the length of the string s and m is the average length of words in word_set.
        """

        # Base case: If the input string is empty, it's considered successfully segmented.
        if not s:
            return True
        
        n = len(s)  # Length of the input string.
        dp = [False] * (n + 1)  # Dynamic programming table to store states.
        dp[0] = True  # Base state: an empty string can always be segmented.

        # Iterate through the string to fill the DP table.
        for i in range(1, n + 1):
            # Attempt to segment the string at different points.
            for j in range(i):
                # If the string up to j cannot be segmented, skip this iteration.
                if not dp[j]:
                    continue

                # Extract the current substring to check.
                word = s[j:i]

                # Check if the current substring is in the word set.
                if word in word_set:
                    # If it is, update the DP table and break to avoid further checks.
                    dp[i] = True
                    break

        # The value at dp[n] indicates whether the whole string can be segmented.
        return dp[n]
    
    def word_set_optimized(s: str, word_set: set) -> bool:
        """
        Determines if the string can be segmented into a sequence of one or more dictionary words,
        using an optimized approach considering the maximum word length in the word_set.

        :param s: The string to be segmented.
        :param word_set: The set containing all the words.
        :return: True if the string can be segmented, False otherwise.

        Time Complexity: O(n * max_length), where n is the length of the string s, 
        and max_length is the length of the longest word in the word_set.
        """

        # Base case: If the input string is empty, it cannot be segmented.
        if not s:
            return False
        
        n = len(s)  # Length of the input string.
        dp = [False] * (n + 1)  # Dynamic programming table to store states.
        dp[0] = True  # Base state: an empty string can always be segmented.

        # Determine the maximum length of words in the word set.
        max_length = max(len(word) for word in word_set) if word_set else 0

        # Iterate through the string to fill the DP table.
        for i in range(1, n + 1):
            # Check substrings of length up to max_length.
            for l in range(1, max_length + 1):
                # Skip if the current length exceeds the substring's start index.
                if i < l:
                    break

                # If the substring ending at i of length l cannot form a word, continue.
                if not dp[i - l]:
                    continue

                # Extract the current substring to check.
                word = s[i - l : i]

                # Check if the current substring is in the word set.
                if word in word_set:
                    # If it is, update the DP table and break to avoid further checks.
                    dp[i] = True
                    break

        # The value at dp[n] indicates whether the whole string can be segmented.
        return dp[n]