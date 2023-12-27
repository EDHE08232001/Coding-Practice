from typing import List

class StoneGame:

    def stone_game(self, a: List[int]) -> int:
        """
        @param a: an array of integers that represents the weights of stones
        @return: the minimum cost to merge all the stones
        """
        n = len(a)
        if n < 2:
            return 0
        
        # pre-optimization
        # range_sum[i][j] => a[i] + a[i + 1] + ... + a[j] 
        range_sum = self.get_range_sum(a)

        # state: dp[i][j] => minimum cost merge from i to j
        dp = [[float('inf')] * n for _ in range(n)]

        # initialization: each sigle stone costs 0 to merge with itself
        for i in range(n):
            dp[i][i] = 0
        
        # enumerate the range size first, then the start point
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for mid in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j] + range_sum[i][j])
        
        return dp[0][n - 1]
    
    def get_range_sum(self, a: List[int]) -> List[List[int]]:
        """
        @param a: an array of intergers that represents the weights of stones
        @return: a list of list of integers

        Returned object: range_sum
        range_sum[i][j] is the sum of from i to j in the list a
        """
        n = len(a)

        # state: range_sum[i][j], sum of from i to j
        range_sum = [[0] * n for _ in range(n)]

        # initialization
        for i in range(n):
            range_sum[i][i] = a[i]

        for i in range(n):
            for j in range(i + 1, n):
                range_sum[i][j] = range_sum[i][j - 1] + a[j]

        return range_sum

stoneArray = [4, 3, 3, 4]
game = StoneGame()
print(game.stone_game(stoneArray))