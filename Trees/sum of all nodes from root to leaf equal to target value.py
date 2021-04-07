def __init__(self):
  self.ans = []
    
def pathSum(self, root, targetSum):
  self.preorder(root,targetSum,[])
  return self.ans


def preorder(self,root,targetsum,res):
  if(not root):
      return

  res.append(root.val)
  if(not root.left and not root.right):
      if(targetsum-root.val==0):
          self.ans.append(list(res))


  self.preorder(root.left,targetsum-root.val,res)
  self.preorder(root.right,targetsum - root.val,res)
  res.pop()   #very vital which pops the last elements which are visisted

  return 
