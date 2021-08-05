from typing import List
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    '''
    step1 need to sort
    step2: index 
    [2,3,6,7],
    
    '''
    candidates.sort()
    res = []
    self.dfs(candidates, target, 0, [], res)
    return res
def dfs(self,candidates, remain, index, path, res):
    if remain == 0:
        res.append(path[:])
        return
    # if remain < 0:
    #     return 
    for i in range(index, len(candidates)):
        if remain - candidates[i] < 0:
            break
        path.append(candidates[i]) 
        self.dfs(candidates, remain - candidates[i], i, path, res)
        path.pop()
    