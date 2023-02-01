def lcsOfStrings(str1,str2):
    longest = ""
    sub_str = ""
    if len(str1) >= len(str2):
        short_str = str2
        long_str = str1
    else:
        short_str = str1
        long_str = str2
    i = 0
    while i < len(short_str):
        k = i
        j = 0
        while (j < len(long_str) and k < len(short_str)):
            if short_str[k] == long_str[j]:
                k += 1
                j += 1
                sub_str = short_str[i:k]
                if len(sub_str) > len(longest):
                    longest = sub_str
            elif len(sub_str) == 0:
                j += 1
            else:
                k = i
                sub_str = ""
        i += 1
    return longest

if __name__ == "__main__":
    str1 = "MABABABN"
    str2 = "XABABY"
    print(lcsOfStrings(str1, str2))
    
