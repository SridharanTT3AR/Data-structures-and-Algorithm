    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if (len(nums)==1):
            return TreeNode(nums[0])
        if (len(nums)==0):
            return None
        half = int(len(nums)/2)
        root = TreeNode(nums[half])
        root.left = self.sortedArrayToBST(nums[:half])
        root.right = self.sortedArrayToBST(nums[half+1:])
        
        return root
      # Note: for a bst preorder and postorder are unique but not inorder.
