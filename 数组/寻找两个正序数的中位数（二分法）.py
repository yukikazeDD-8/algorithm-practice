def searchmedianarry(nums1,nums2):
    if len(nums1)>len(nums2):
        nums1,nums2=nums2,nums1
    m,n=len(nums1),len(nums2)
    total=n+m
    half=(total+1)//2
    #left是数组1的左边界，right是数组1的右边界
    left,right=0,m

    while left<right:
        i=(right+left)//2
        j=half-i

        # 四个边界值（处理越界）
        left1 = float('-inf') if i == 0 else nums1[i - 1]
        right1 = float('inf') if i == m else nums1[i]
        left2 = float('-inf') if j == 0 else nums2[j - 1]
        right2 = float('inf') if j == n else nums2[j]

        if left1<right2 and left2<right1:
            if total%2==0:
                return (max(left1,left2)+min(right1,right2))/2
            elif total%2!=0:
                return max(left1,left2)
        elif left1>right2:
            right=i-1
        else:
            left=i+1
    return 0

line1=input('请输入数组1:')
nums1=list(map(int,line1.split()))

line2=input('请输入数组2:')
nums2=list(map(int,line2.split()))

result=searchmedianarry(nums1,nums2)
print('中位数是：',result)

