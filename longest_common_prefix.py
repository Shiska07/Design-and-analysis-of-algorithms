class Solution(object):
    def longestCommonPrefix(self, strs):
        longest = []
        for item in strs:
            k = 0
            i = 1
            count = 0
            pre = []  # prefix list
            pre.append(0)
            while i < len(item):
                if item[i] == item[k]:
                    pre.append(pre[i - 1] + 1)
                    i += 1
                    k += 1
                else:
                    if pre[i - 1] > count:
                        count = pre[i - 1]
                    k = pre[k - 1]
            longest.append(count)
        min = min(longest)
