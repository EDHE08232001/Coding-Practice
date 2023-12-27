from typing import List

class BinarySearch:

    def binary_search(self, nums: List[int], target: int):
        """
        @param nums: a list of sorted integers
        @param target: an integer
        @return: the index of the target number
        """
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        
        return -1
    
intArray = [2, 5, 6, 11, 20, 35, 50]
obj = BinarySearch()
print(obj.binary_search(intArray, 20))