class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        curnode  = root
        mapping = {}
        maprow = {}
        q = []
        mapping[root] = 0
        maprow[root] = 0
        
        q.append(root)
        
        while(q):
            curnode = q.pop(0)
            if(curnode.left):
                mapping[curnode.left] =  mapping[curnode] - 1
                maprow[curnode.left] =  maprow[curnode] + 1
                q.append(curnode.left) 
            if(curnode.right):
                mapping[curnode.right] =  mapping[curnode] + 1
                maprow[curnode.right] =  maprow[curnode] + 1
                q.append(curnode.right) 
            
        list_value = sorted(set(mapping.values()))
        result = []
        
        for val in list_value:
            ans1 = []
            ans = []
            for key,value in mapping.items():
                
                if(val == value):
                    ans.append((key.val,maprow[key]))
            if len(ans)>0:
                ans = sorted(ans, key = lambda k1 : (k1[1],k1[0]))
            
            
            for i in range(len(ans)):
                print(ans[i][0])
                ans1.append(ans[i][0])
            result.append(ans1)
            
        return result
                
