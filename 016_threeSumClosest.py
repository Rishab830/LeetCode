class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        diff = abs(nums[0] + nums[1] + nums[2] - target)
        sum = nums[0] + nums[1] + nums[2]
        if diff == 0:
            return target
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                val = nums[left] + nums[right] + nums[i]
                if diff > abs(target - val):
                    diff = abs(target - val)
                    sum = val
                if val < target:
                    left += 1
                elif val > target:
                    right -= 1
                else:
                    return target
        return sum