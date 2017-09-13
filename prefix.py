class Solution(object):
    def longestCommonPrefix(self, strs):
        strs = {"test", "tst", "testing"}
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].index(prefix) != 0:
                
    print(longestCommonPrefix(0, input()))