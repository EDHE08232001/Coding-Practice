from typing import List

class CopyBooks:
    def copy_books(self, pages: List[int], k: int) -> int:
        """
        Calculate the minimum time required to copy all books given k people, where each person
        can copy a contiguous sequence of books, and the time taken is the sum of the pages in the sequence.

        :param pages: A list of integers where each element represents the number of pages in a book.
        :param k: The number of people available to copy the books.
        :return: The minimum time required to copy all books.

        The function utilizes dynamic programming to calculate the minimum time. It constructs a
        2D array dp where dp[i][j] represents the minimum time to copy the first i books using j people.
        """

        # Base case: if there are no pages or no people, return 0 as no copying is needed.
        if not pages or not k:
            return 0
        
        n = len(pages)  # Total number of books.

        # Calculate prefix sums for the pages to quickly find the sum of pages between any two books.
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + pages[i - 1]

        # Initialize the DP table where dp[i][j] represents the minimum time to copy the first i books with j people.
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

        # Base case initialization: 0 books take 0 time to copy regardless of the number of people.
        for i in range(k + 1):
            dp[0][i] = 0

        # Fill the DP table: iterate over each book and each person.
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Iterate over all possible previous books to find the minimum time.
                for prev in range(i):
                    # Calculate the cost (time) to copy from the 'prev' book to the 'i'th book.
                    cost = prefix_sum[i] - prefix_sum[prev]
                    # Update the DP table with the minimum time.
                    dp[i][j] = min(dp[i][j], max(dp[prev][j - 1], cost))
        
        # The answer is the minimum time to copy all n books using k people.
        return dp[n][k]
