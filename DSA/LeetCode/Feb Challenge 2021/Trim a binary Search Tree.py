root = [1,0,2]
low = 1
high = 2

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def trimBST(self,root,low,high):
        if self.root is None:
            return None
        p = self.root
        if p.data>high:
            pass

            








