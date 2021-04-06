    def maxPathSum(self, root: TreeNode) -> int:
        global max_sum
        max_sum = float('-inf')
        self.maximum_value(root)
        return max_sum
        
        
    def maximum_value(self,root):
        global max_sum
        if not root:
            return 0
        #to find maximmum value from left sub tree
        left_tree = max(self.maximum_value(root.left),0)
        #to find maximmum value from right sub tree
        right_tree = max(self.maximum_value(root.right),0)
        
        #finding the current maximum path sum
        current_node_max_path_sum = left_tree + right_tree + root.val
        max_sum = max(max_sum,current_node_max_path_sum)
        return root.val + max(left_tree,right_tree)
