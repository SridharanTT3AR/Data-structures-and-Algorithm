def checkBST(root):
    
    result = inordertraversal(root)
    for i in range(1,len(result)):
        if(result[i]-result[i-1]<=0):
            return False
    return True
    

def inordertraversal(root):
    arr = []
    if (root):
        arr = arr + inordertraversal(root.left)
        arr.append(root.data)
        arr = arr + inordertraversal(root.right)
    return arr
