class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            target = -nums[k]
            left = k + 1
            right = len(nums) - 1
            while left < right:
                val = nums[left]+nums[right]
                if val < target:
                    left += 1
                elif val > target:
                    right -= 1
                else:
                    ans.append([nums[k], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
        return ans