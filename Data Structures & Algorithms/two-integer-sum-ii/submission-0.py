class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #since the array is sorted, so the best approach, I can see here is 
        #considering two pointers left pointer and the right pointer
        #and then start trading from both the ends until these two pointers did not meet 
        #now, we keep adding these two values until we get to the target
        #in this process, if we find the the target to be greater than the sum then
        #we move the left pointer to the right side that is increment the left pointer
        #if we find that the target is lesser than a sum, then we move the right pointer to the left
        #that is we decrement the right pointer
        #and if the sum is equal to the target, then we return the indicis of these two pointers
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if target > sum:
                l += 1
            elif target < sum:
                r -= 1
            else:
                return[l + 1, r + 1]
            
