def solution(A):
    '''
    input: a list a distance of bike aready allocated form start point 0
    output : find a empty position to attach your bike which is largest possible distance form any other bike
    idea:The longest distance between parked bikes should be the middle of two parked bikes
    so need to calculate the max intervals between them and divide by 2.
    A = [10, 0, 8, 2, -1, 12, 11, 3]
    A = [-1, 0, 2, 3, 8, 10, 11, 12]
         # # _ # # _ _ _ _ # _ #  #  #    which _ is empty, # is occuped
        -1 0 1 2 3 4 5 6 7 8 9 10 11 12
    my solution: 1: sorted first to get a acceding order of distance from point 0
                 2: for loop the sorted arr and use a v variable max_dis to record the  max possivble distance form any other bike
 
    sorted(A) 
    space：quicksort（）
    time:(NlogN)
    space: O(N)/ O(1)
    Sorting - space 
    Average-case Time = O(nlogn)
    Worst-case Time = O(n^2)
    '''

    A.sort()
    res = 0
    
    for index in range(1, len(A)):
        distance = (A[index] - A[index - 1]) // 2
        res = max(res, distance)
    return res
