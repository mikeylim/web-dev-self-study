class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] is nums[i + 1]:
                i = i + 1
            else:
                return nums[i]

sol = Solution()
print(sol.singleNumber([2,2,3,4,3,4,5]))