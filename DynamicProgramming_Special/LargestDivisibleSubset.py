from typing import List, Dict

class LargestDivisibleSubset:
    def largest_divisible_subset(self, nums: List[int]) -> List[int]:
        """
        Finds the largest subset of nums where every pair of elements is divisible.
        
        @param nums: List[int] - The input list of numbers.
        @return: List[int] - The largest divisible subset.
        
        Time Complexity: O(n^2), where n is the length of nums.
        Space Complexity: O(n), for storing dp and prev arrays.
        """
        # Sort the numbers to ensure the divisible pairs are found correctly.
        nums = sorted(nums)
        n = len(nums)
        
        # dp[i] will hold the maximum length of the divisible subset ending with nums[i].
        dp = [1] * n
        # prev[i] will hold the index of the previous element in the subset for nums[i].
        prev = [-1] * n

        # Initialize the index of the last element in the largest subset found.
        last_index = 0
        for i in range(1, n):
            for j in range(i):
                # Check if nums[i] is divisible by nums[j] and update dp[i] and prev[i] accordingly.
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            # Update the index of the last element if a larger subset is found.
            if dp[i] > dp[last_index]:
                last_index = i

        # Reconstruct the largest divisible subset.
        subset = []
        while last_index != -1:
            subset.append(nums[last_index])
            last_index = prev[last_index]
        
        return subset[::-1]
    
    def largest_divisible_subset_optimized(self, nums: List[int]) -> List[int]:
        """
        Optimized method to find the largest divisible subset using a hashmap.
        
        @param nums: List[int] - The input list of numbers.
        @return: List[int] - The largest divisible subset.
        
        Time Complexity: O(n * sqrt(max(nums))), which is faster than the previous method for large inputs.
        Space Complexity: O(n), for storing dp and prev dictionaries.
        """
        if not nums:
            return []
        
        # Sort the numbers to ensure the divisible pairs are found correctly.
        nums = sorted(nums)
        # Initialize dp and prev dictionaries to store the length of the largest subset and previous number respectively.
        dp, prev = {}, {}
        for num in nums:
            dp[num] = 1
            prev[num] = -1

        last_num = nums[0]
        for num in nums:
            for factor in self._get_factors(num):
                # Update dp and prev if a larger subset ending with num is found.
                if factor in dp and dp[num] < dp[factor] + 1:
                    dp[num] = dp[factor] + 1
                    prev[num] = factor
            # Update the last number if a larger subset is found.
            if dp[num] > dp[last_num]:
                last_num = num

        # Reconstruct the largest divisible subset.
        return self._get_path(prev, last_num)
    
    def _get_path(self, prev: Dict, last_num: int) -> List[int]:
        """
        Helper function to reconstruct the path from the prev dictionary.
        
        @param prev: Dict - The dictionary holding previous elements.
        @param last_num: int - The last number in the subset.
        @return: List[int] - The reconstructed path.
        """
        path = []
        while last_num != -1:
            path.append(last_num)
            last_num = prev[last_num]
        return path[::-1]
    
    def _get_factors(self, num: int) -> List[int]:
        """
        Helper function to find all factors of a given number.
        
        @param num: int - The number to find factors of.
        @return: List[int] - The list of factors.
        """
        if num == 1:
            return []
        
        factor = 1
        factors = []
        while factor * factor <= num:
            if num % factor == 0:
                factors.append(factor)
                if factor * factor != num and factor != 1:
                    factors.append(num // factor)
            factor += 1
        
        return factors