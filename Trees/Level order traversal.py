class Queue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def enqueue(self, data):
        self.items.append(data)
 
    def dequeue(self):
        return self.items.pop(0)
    
    def length(self):
        return len(self.items)

class Solution:
    def levelOrder(self, root):      
        result = []
        if(root is None):
            return result
        q = Queue()
        q.enqueue(root)
        while(not q.is_empty()):
            l = q.length()
            currlist = []
            for i in range(l):
                curnode = q.dequeue()
                currlist.append(curnode.val)
                if(curnode.left):
                    q.enqueue(curnode.left)
                if(curnode.right):
                    q.enqueue(curnode.right)
            
            result.append(currlist)
        return result
            
