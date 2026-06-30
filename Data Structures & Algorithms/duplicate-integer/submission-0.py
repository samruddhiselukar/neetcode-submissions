class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort() #O(nlogn)
        # for i, a in enumerate(nums): #O(n)
        #     if i > 0 and a == nums[i - 1]:
        #         return True
        # return False

        # dict = {}
        # for a in nums:
        #     if a in dict:
        #         dict[a] += 1
        #     else:
        #         dict[a] = 1
        #     if dict[a] > 1:
        #         return True
        # return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
            
        