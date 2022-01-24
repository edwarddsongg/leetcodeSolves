class Solution(object):
    def singleNumber(self, nums):
        nums.sort()

        for i in nums:
            print(i)

        l = len(nums)-1
        i=0

        while True:
            if i+1 > l-1:
                return nums[i]
            elif nums[i] == nums[i+1]:
                i+=2
                print(f"in:{i}")
            else:
                print(f"ins:{ nums[i]} k: {nums[i+1]}")
                return nums[i]
        
n = Solution()
print(f"test: {n.singleNumber([4, 1, 2, 1, 2])}")

