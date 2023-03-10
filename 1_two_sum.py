# from typing import List

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            num1 = nums[i]
            d_value = target - num1
            if d_value in d:
                return [d[d_value], i]
            d[num1] = i

        return []


if __name__ == '__main__':
    instance1 = Solution()

    print("Case 1:", instance1.twoSum([2, 7, 11, 15], 9))
    print("Case 2:", instance1.twoSum([3, 2, 4], 6))
    print("Case 3:", instance1.twoSum([3, 3], 6))
