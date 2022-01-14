from typing import List
import math


class Solutions(object):
    def isPalindrome(self, x):
        if str(x) ==  str(x)[::-1]:
           return True
        else:
            return False

class Solution(object):
    def isPalindrome(self, x):
        numList = []
        
        if x < 0:
            return False
        elif x<10 == 0:
            return True
        else:

            lenN = int(math.log10(x))+1
            for i in range(lenN):
                num = math.floor(x%(10))
                numList.append(num)
                x=math.floor(x/10)
             
            return (numList[::-1] == numList)
        






        
        