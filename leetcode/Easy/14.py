def longest_common_prefix(strs):
    if not strs:
        return ""

    lcp = ""
    first_word = strs[0]


    for i in range(len(first_word)):
        current_char = first_word[i]


        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != current_char:
                return lcp  

        lcp += current_char  

    return lcp

print(longest_common_prefix(["dog","racecar","car"]))
print(longest_common_prefix(["flower","flow","flight"]))