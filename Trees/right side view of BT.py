def rightSideView(self, root) -> List[int]:
        if not root:
            return None
        q = []
        result=[]
        result.append(root.val)
        q.append(root)
        while q:
            temp = []
            for i in range(len(q)):
                curnode = q.pop(0)
                if(curnode.left):
                    q.append(curnode.left)
                    temp.append(curnode.left.val)
                if(curnode.right):
                    q.append(curnode.right)
                    temp.append(curnode.right.val)
            if(len(temp)>0):
                result.append(temp[-1])
        return result
      
      # append all the last element of the level order 
