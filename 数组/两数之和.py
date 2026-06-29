def two_sum(num,target):
    n=len(num)
    for i in range(n):
        for j in range(i+1,n):
            if num[i]+num[j]==target:
                return [i,j]

target=int(input('输入目标数'))

line = input('请输入数组：')
num= line.split()
num = list(map(int, num))

result=two_sum(num,target)
print(result)

