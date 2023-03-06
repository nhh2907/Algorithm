# My code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        for idx, num in enumerate(nums):
            check = target - num
            if check == nums[idx]:
                count += 1
                if count == 2:
                    beta = nums.index(check)
                    return idx, beta
                continue
            if check in nums:
                beta = nums.index(check)
                return idx, beta


# Bst code I think
myHash = {}
    for index, value in enumerate(nums):
        if target - value in myHash:
            return [myHash[target-value], index]
        myHash[value] = index
