class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str_num = str(num) [::-1]
        
        ones = ["I", "II", "III"]
        num_arr = [['I', 'V', 'X'], ['X', 'L', 'C'], ['C', 'D', 'M'], ['M']]
        roman = ""
        for i, l in enumerate(str_num):
            if l == '4':
                roman = num_arr[i][0] + num_arr[i][1] + roman
            elif l == '9':
                roman = num_arr[i][0] + num_arr[i][2] + roman
            elif l == '5':
                roman = num_arr[i][1] + roman
            elif int(l) > 5:
                for k in range(int(l)-5):
                    roman = num_arr[i][0] + roman 
                roman = num_arr[i][1] + roman  
            elif int(l) < 5:
                for k in range(int(l)):
                    roman = num_arr[i][0] + roman 
        
        return roman


        #for i in str(num)



to = Solution()
to.intToRoman(599)
