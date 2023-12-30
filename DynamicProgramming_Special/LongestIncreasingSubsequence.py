from typing import List

class LongestIncreasingSubsequence:
    def longestIncreasingSubsequence(self, nums: List[int]) -> int:
        """
        Calculate the length of the longest increasing subsequence in a given list of integers.

        This method uses dynamic programming. The `dp` array at index `i` stores the length of the
        longest increasing subsequence ending with `nums[i]`. The function iterates through each
        number, updating the `dp` array based on previously computed values.

        Args:
            nums (List[int]): The list of integers representing the sequence.

        Returns:
            int: The length of the longest increasing subsequence in the given sequence.

        Time Complexity:
            O(n^2), where n is the length of the input list.

        Space Complexity:
            O(n), where n is the length of the input list.
        """
        # Handle the edge case of an empty list.
        if not nums:
            return 0

        # Initialize the dp array with 1s, as each number is a subsequence of length 1.
        dp = [1] * len(nums)

        # Build the dp array.
        for i in range(len(nums)):
            for j in range(i):
                # If nums[j] is less than nums[i], it can form an increasing subsequence.
                if nums[j] < nums[i]:
                    # Update dp[i] to the maximum length found so far.
                    dp[i] = max(dp[i], dp[j] + 1)

        # The result is the maximum length found in the dp array.
        return max(dp)

    def longest_increasing_subsequence_optimized(self, nums: List[int]) -> int:
        """
        An optimized version of the longest increasing subsequence using binary search.

        Instead of using a standard dp array, this method maintains an array `lis` where `lis[i]`
        represents the smallest ending number of an increasing subsequence of length `i`.

        Args:
            nums (List[int]): The list of integers representing the sequence.

        Returns:
            int: The length of the longest increasing subsequence.

        Time Complexity:
            O(n log n), where n is the length of the input list.

        Space Complexity:
            O(n), where n is the length of the input list.
        """
        # Handle the edge case of an empty list.
        if not nums:
            return 0

        # Initialize the lis array with infinity, setting the first element to negative infinity.
        lis = [float('inf')] * (len(nums) + 1)
        lis[0] = -float('inf')

        longest = 0
        for num in nums:
            # Find the first index in `lis` where the number is greater than or equal to `num`.
            index = self._first_gte(lis, num)
            # Update the `lis` array with the new number.
            lis[index] = num
            # Update the length of the longest increasing subsequence found so far.
            longest = max(longest, index)

        return longest

    def _first_gte(self, nums: List[int], target: int) -> int:
        """
        Find the first index in a list where the number is greater than or equal to the target.

        Args:
            nums (List[int]): The list of numbers to search.
            target (int): The target number.

        Returns:
            int: The index of the first number in `nums` that is greater than or equal to `target`.
        """
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        # Determine which index meets the condition.
        if nums[start] >= target:
            return start
        return end