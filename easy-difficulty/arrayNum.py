class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        tens = 1
        ind = 0
        arr = []
        carry = 0

        temp = 0
        while k > 0 or carry != 0:
            number = k % 10 
            k -= k% 10
            k /= 10
            k = int(k)
            print("tp"+ str(number))
            if(ind < len(num)):
                print("int" + str(ind))
                number += num[len(num) - 1 - ind]
                print(str(carry) +  "yo" + str(number))
                num[len(num) - 1 - ind] = number - 10 + carry if number + carry >= 10 else number + carry
                carry = 1 if number >= 10 else 0
                print("carry:" + str(carry))
                
            else:
                print(str(carry) +  "yos" + str(number))
                num.insert(0, number + carry) 
                carry = 1 if number >= 10 else 0

            
            ind += 1
    
        
        return num

s1 = Solution()

yo = s1.addToArrayForm([9,9,9], 1)
for i in yo:
    print(i)