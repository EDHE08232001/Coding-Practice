from typing import List

class RussianDollEnvelopes:
    def max_envelopes(self, envelopes: List[List[int]]) -> int:
        """
        Calculates the maximum number of envelopes that can be nested inside each other.

        Args:
            envelopes (List[List[int]]): A list of envelopes represented as pairs of width and height.

        Returns:
            int: The maximum number of nested envelopes.

        Time Complexity: O(n*log(n)), where 'n' is the number of envelopes.
        """
        if not envelopes:
            return 0
        
        # Sort envelopes by width in ascending order and by height in descending order.
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        n = len(envelopes)
        # Initialize an array to track the longest increasing subsequence.
        longest_increasing_subsequence = [float('inf')] * (n + 1)
        longest_increasing_subsequence[0] = -float('inf')

        longest = 0
        for (_, h) in envelopes:
            # Find the index where the current envelope's height can be inserted.
            index = self._get_gte(longest_increasing_subsequence, h)
            longest_increasing_subsequence[index] = h
            longest = max(longest, index)

        return longest
    
    def _get_gte(self, nums: List[int], target: int) -> int:
        """
        Binary search for the index of the first element in 'nums' greater than or equal to 'target'.

        Args:
            nums (List[int]): List of integers to search in.
            target (int): The target value.

        Returns:
            int: The index of the first element greater than or equal to 'target'.
        """
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] >= target:
            return start
        return end
