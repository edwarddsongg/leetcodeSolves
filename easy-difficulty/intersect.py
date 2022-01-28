class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        
        l = len(nums1)
        
        hash_dict = {}
        for i in nums1:
            if i in hash_dict:
                hash_dict[i]+=1
            else:
                hash_dict[i]=1
        
        index = 0;
        
        for i in nums2:
            if i in hash_dict:
                if hash_dict[i]>0:
                    nums1[index] = i
                    index+=1
                    hash_dict[i]-=1
        
        return nums1[:index]
            
        
            
        