class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = [["(", ")"], ["{", "}"], ["[", "]"]]
        forward = []
        index = 0
        for i in s:
            if i == arr[0][0]:
                forward.append(arr[0][0])
            elif i == arr[1][0]:
                forward.append(arr[1][0])
            elif i == arr[2][0]:
                forward.append(arr[2][0])

            print(len(forward))

        index = len(forward) - 1

        for i in s:
            if i == arr[0][1]:
                if len(forward) != 0  and forward[index] == "(":
                    index-=1
                else:
                    return False
            elif i == arr[1][1]:
                if len(forward) != 0 and forward[index] == "{":
                    index-=1
                else:
                    return False
            elif i == arr[2][1]:
                if len(forward) != 0 and forward[index] == "[":
                   index-=1
                else:
                    return False
            
        if len(forward) == 0:
            return True
        else:
            return False
