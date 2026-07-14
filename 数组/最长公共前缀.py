def longestCommonPrefix(strs):
    first=strs[0]
    for i,s in enumerate(first):
        for j in strs[1:]:
            if i>len(j) or j[i]!=s:
                return first[:i]
    return first

strs=input('请输入字符串（空格分隔）:').split()
print(longestCommonPrefix(strs))