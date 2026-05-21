import math
import copy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            nums2 = nums.copy()
            nums2.remove(i)
            res.append(math.prod(nums2))
        return res



        