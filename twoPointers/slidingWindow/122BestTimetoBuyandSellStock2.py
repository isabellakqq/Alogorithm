
def maxProfit(prices) -> int:
    '''
        [7,1,5,3,6,4]
            ^.^
    find valley and peak

    prices[i] - buy
    
    '''
    n = len(prices)
    i = 0
    valley = prices[0]
    peak = prices[0]
    maxprofit = 0
    while i < n - 1:
        # while 满足条件 一定要加上最外层的while条件
        # i不一定更新多少所以不适合forloop
        # 用while的时候前面越界判断
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1
        valley = prices[i]
        
        while i < n - 1 and prices[i] <= prices[i + 1]:
            i += 1
            
        peak = prices[i]
        
        maxprofit += peak - valley
    
    return maxprofit
    
    
#         n = len(prices)
#         if  n < 2:
#             return 0
#         maxprofit = 0
#         for i in range(1, n):
#             if prices[i] > prices[i - 1]:
#                 maxprofit += prices[i] - prices[i - 1]
            
#         return maxprofit
    