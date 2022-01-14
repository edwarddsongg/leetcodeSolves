class Solution(object):
    def removeDuplicates(self, nums):
        if(len(nums) == 0):
            print(0)
        
        prev = nums[0]
        ind = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i]!=prev:
                prev = nums[i] 
                nums[ind] = nums[i]  
                count+=1
                ind+=1
        return nums


s1 = Solution()
print(s1.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
            
        