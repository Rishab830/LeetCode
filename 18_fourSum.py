class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    val = nums[left] + nums[right] + nums[i] + nums[j]
                    if val < target:
                        left += 1
                    elif val > target:
                        right -= 1
                    else:
                        ans.append([nums[left], nums[right], nums[i], nums[j]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        left += 1
        return ans