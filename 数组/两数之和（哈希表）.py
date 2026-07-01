def two_sum_hash(nums,target):
    hash_map={}                             #设置一个空字典用来存储键值对（数据：下标）
    for i,num in enumerate(nums):           #使用enumerate（）同时获取下标和数
        need=target-num                     #need用来在字典中另一半
        if need in hash_map:
            return (hash_map[need],i)       #找到则返回另一半的下标以及当前数的下标
        else: hash_map[num]=i
    return []

target=int(input('请输入目标数'))
line=input('请输入数组')
nums=list(map(int,line.split()))

result=two_sum_hash(nums,target)
print(result)
