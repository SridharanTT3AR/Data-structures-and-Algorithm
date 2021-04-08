def __init__(self):
    self.ans = 0
def sumNumbers(self, root: TreeNode) -> int:
    self.answer(root,"")
    return self.ans

def answer(self,root,value):
    if not root:
        return
    value+=str(root.val)
    if(not root.left and not root.right):
        self.ans+=int(value)

    self.answer(root.left,value)
    self.answer(root.right,value)
    value = value[:len(value)-1]

    return
