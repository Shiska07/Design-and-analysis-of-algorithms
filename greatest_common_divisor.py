class Solution(object):
    def gcdOfStrings(self, str1, str2):
        greatest = ""
        
        if len(str1) >= len(str2):
            l = str1
            s = str2  
        else:
            l = str2
            s = str1
        
        # reversed strings
        l_rev = l[::-1]
        s_rev = s[::-1]
        
        sub_str = ""
        
        i = 1
        while i <= len(s):
            sub_str = s[0:i]
            if (s[0:i] == sub_str) and (l[0:i] == sub_str) and (s_rev[0:i] == sub_str[::-1]) and (l_rev[0:i] == sub_str[::-1]):
                greatest = sub_str
                i = i + 1
            else:
                if len(greatest) == 0:
                    i = i + 1
                else:
                    return greatest
        return greatest

if __name__ == "__main__":
    str1 = "ABABABAB"
    str2 = "ABAB"
    mysoln = Solution()
    print(mysoln.gcdOfStrings(str1, str2))
