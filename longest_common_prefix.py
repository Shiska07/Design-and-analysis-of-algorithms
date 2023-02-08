class Solution(object):
    def longestCommonPrefix(self, strs):
        n = len(strs)
        i = 0
        match = 1
        count = 0
        len_smallest = len(strs[0])
        for item in strs:
            if len(item) < len_smallest:
                len_smallest = len(item)
        while i < len_smallest:
            j = 1
            while j < n:
                match = (strs[0][i] == strs[j][i])
                if match:
                    j += 1
            if j == n:
                count += 1
                i += 1
            else:
                break
        if count > 0:
            return strs[0][0:count]
        else:
            return ""
