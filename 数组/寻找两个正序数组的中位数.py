def searchmedianarry(nums1,nums2):
    merged=[]       #合并后的数组
    i,j=0,0         #i，j分别用来记录两个数组遍历的下标

    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1

    #while循环结束后将剩余的部分添加到数组末尾
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])

    n=len(merged)
    #判断数组长度的奇偶
    if n%2==0:
        mid=(merged[n//2-1]+merged[n//2])/2
    else:
        mid=merged[n//2]
    return mid

line1=input('请输入递增数组1：')
nums1=list(map(int,line1.split()))

line2=input('请输入递增数组2：')
nums2=list(map(int,line2.split()))

result=searchmedianarry(nums1,nums2)
print('中位数是',result)
input('按回车键退出...')
