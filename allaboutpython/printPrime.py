
n = int(input())
for i in range(2, n + 1): # 使用for循环遍历区间[2,n]
    isPrime = True
    for j in range(2, int(pow(i, 0.5)) + 1): # 在 2 到 sqrt(i) 中判断有无 i 的因子
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i)