#using list

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=0
        n=len(nums)
        for i in range(n):
            complement=target-nums[i]
            if complement in nums:
                a=nums.index(complement)
                if a==i:
                    continue
                break
        return i,a