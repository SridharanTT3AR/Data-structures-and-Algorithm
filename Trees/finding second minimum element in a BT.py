#root.val = min(root.right.val,root.left.val) is been followed
def findSecondMinimumValue(self, root) -> int:
        self.ans = float('inf')
        first_minimum = root.val
        def ordering(root):
            if(root):
                if(first_minimum<root.val<self.ans):
                    self.ans = root.val
                ordering(root.left)
                ordering(root.right)
        ordering(root)
        
        return self.ans if self.ans < float('inf') else -1
