class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        temp = ""
        if len(strs) == 0:
            return ""
                
        smallest = strs[0]

        for word in strs:
            if len(word) < len(smallest):
                smallest = word

        for i in range(len(smallest)):
            for word in strs:
                if smallest[i] != word[i]:
                    return prefix
            prefix += smallest[i]
            

        return prefix


a = {}
a[0] = "top"
a[10] = "to"
for i in a:
    print(i)