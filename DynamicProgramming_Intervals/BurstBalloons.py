from typing import List


class BurstBalloons:

  def max_coins(self, nums: List[int]) -> int:
    """
    This function calculates the maximum number of coins that can be obtained
    by bursting balloons. Each balloon has a number of coins associated with it,
    and bursting a balloon i gives coins equal to nums[i-1] * nums[i] * nums[i+1].
    Once a balloon is burst, it's removed from the sequence.

    Args:
    nums (List[int]): A list of integers representing the number of coins in each balloon.

    Returns:
    int: The maximum coins that can be obtained by bursting the balloons wisely.
    """

    # Padding the list with 1 on both ends to simplify calculations for edge balloons
    nums = [1, *nums, 1]
    n = len(nums)

    # Initialize a 2D DP array to store the maximum coins obtainable from bursting balloons i to j
    dp = [[0] * n for _ in range(n)]

    # Iterate over the length of the subarray of balloons considered
    for length in range(3, n + 1):
      # Iterate over all possible starting points for the current length
      for i in range(n - length + 1):
        # Calculate the ending index based on the starting index and length
        j = i + length - 1
        # Iterate over all possible positions k to burst the last balloon in the range (i, j)
        for k in range(i + 1, j):
          # Update the DP table with the maximum coins obtained by choosing a different k
          dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])

    # The maximum coins obtainable from bursting all balloons is in dp[0][n-1]
    return dp[0][n - 1]
