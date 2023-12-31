class EditDistance:

  def min_distance(self, word1: str, word2: str) -> int:
    """
    @param word1: a string
    @param word2: a string
    @return: the minimum distance between the two words,
             or the minnimum amount of times required to
             transform word1 into word2.
    """
    if word1 is None or word2 is None:
      return -1

    n, m = len(word1), len(word2)

    # state
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # initialization
    for i in range(n + 1):
      # need i deletions to transform first i characters
      # in word1 into first 0 characters in word2 
      dp[i][0] = i
    for j in range(m + 1):
      # need j insertions to transform first 0 characters
      # in word1 into first j characters in word2
      dp[0][j] = j

    # function
    for i in range(1, n + 1):
      for j in range(1, m + 1):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        if word2[j - 1] == word1[i - 1]:
          dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
        else:
          dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1)

    return dp[n][m]
