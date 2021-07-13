class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        clarify:sanity check duplicate
        find distance from next greater one for each arr[i]
       Traverse the daily temperature. If the temperature of the current day is greater than the temperature of the stack[-1], it means that the day is the warming day of stack[-1]. Therefore, the top element of the stack is removed from the stack, and the difference between the number of days and the current day is calculated and stored in the result. Noincresing monotonic stack
        res:high level logic:use monic stack to store index i which tmp[i] > top of
        midium level logic: while not stack or tmp[i] > stack[-1] upadate res[i] == i - stack[-1]
          [73,74,75,71,69,72,76,73]
            i = 0, stack [0]
            i = 1  T[0] < 74 stack.pop() = 73 stack = [74] res[0] = 1
            i = 2 stack = [0] res[1] = 1
            i = 3 stack = [1]
            i = 4 stack = [2, 3, 4]
            i = 5 stack = [2,  5] res[4] = 1 res[3] = 2
            i = 6 stack =  [6] res [5] = 1 res[2] = 4
            i = 7  stack = [6, 7]
        test:
        '''
        
        if not temperatures:
            return None
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i, n in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < n:
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)
        return res
            
        