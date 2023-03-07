class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = [["(", ")"], ["{", "}"], ["[", "]"]]
        forward = []

        for i in s:
            if i == arr[0][0]:
                forward.append(arr[0][0])
            elif i == arr[1][0]:
                forward.append(arr[1][0])
            elif i == arr[2][0]:
                forward.append(arr[2][0])
            
            print(len(forward))

            if i == arr[0][1]:
                if len(forward) != 0 == "[" and forward[len(forward)-1]:
                    print("yo")
                    forward.pop(len(forward) - 1)
                else:
                    break
            elif i == arr[1][1]:
                if len(forward) != 0 == "[" and forward[len(forward)-1]:
                    forward.pop(len(forward) - 1)
                else:
                    break
            elif i == arr[2][1]:
                if len(forward) != 0 == "[" and forward[len(forward)-1]:
                    forward.pop(len(forward) - 1)
                else:
                    break
            
        if len(forward) == 0:
            return True
        else:
            return False


yo = Solution()
print(yo.isValid("()"))