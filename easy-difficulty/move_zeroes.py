class Solution(object):
    def moveZeroes(self, nums):
        l = len(nums)
        tail = l-1
        head = 0
        count = 0

        for i in range(l):
            if nums[i]==0:
                count+=1
            
            if  i + count>=l-1:
                nums[i] == 0
            else:
                nums[i] = nums[i+count]

        print(*nums)

            

                

n = Solution()
n.moveZeroes([0, 1, 0, 3, 12])
