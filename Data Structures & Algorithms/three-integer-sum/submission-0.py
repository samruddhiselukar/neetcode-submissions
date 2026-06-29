class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #the first approach is a brute force approach I can see is taking three pointers like a 3 for loops
        #and I trading through the complete array, checking if the turn out to be zero, and if it does
        #we will return the triplets
        #this approach is not optimal. It is having the time complexity of O(n^3)

        #optimal
        #so the optimal approach will go like first of all, we will sort the array
        #next by element in the considering the first element as one number in the triplet
        #and the rest 2 sum, we can follow the two SUM approach.
        #first, let's sort the array
        nums.sort()
        res = []

        #now, let's use a for loop 
        for i, a in enumerate(nums): #[-4,-1,-1,0,1,2]
            #here we need to give a condition that if I is greater than zero and the element at
            #I -1 is equal to the element at I then continue
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        return res
            

        

