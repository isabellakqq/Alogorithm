class Solution:
    '''
    clarify: treeNode roor, list of list
    result:dfs to find all locations in the list and then traverse throung the location in sorted order
    test [(0, 0, 3), (1, -1, 9), (1, 1, 20), (2, 0, 15), (2, 2, 7)]
    '''
    #O(NlogN) time
    def verticalTraversal(self, root):
        node_list = []
        self.dfs(root, 0, 0, node_list)
        node_list.sort()
        res = []
        col_index = node_list[0][0]
        tmp = []
        for col, row, val in node_list:
            if col == col_index:
                tmp.append(val)
            else:
                res.append(tmp)
                col_index = col
                tmp = [val]
        res.append(tmp)
        return res
    def dfs(self, root, col, row, node_list):
        if root:
            node_list.append(root, col, row, root.val)
            self.dfs(root.left, col - 1, row + 1, node_list)
            self.dfs(root.right, col + 1, row + 1, node_list)



            

            