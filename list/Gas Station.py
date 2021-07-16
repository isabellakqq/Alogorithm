from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        clarify:
             guaranteed to be unique
             

        gas = [1,2,3,4,5],
        cost = [3,4,5,1,2]
        the sum of gas minus sum of cost less than 0 
        
        '''
        #case1
        if sum(gas) - sum(cost) < 0:
            return -1
        remain = 0
        start = 0
        #case2
        for i in range(len(gas)):
            if remain + gas[i] < cost[i]:
                start = i + 1
                remain = 0
            else:
                remain += gas[i] - cost[i]
        return start