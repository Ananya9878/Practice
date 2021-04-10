class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def rightSideView(self, root):
        if root is None:
            return []
        s = [root]
        t = [root.val]
        while len(s) > 0:
            temp = []

            for i in s:
                if i.left is not None:
                    temp.append(i.left)
                if i.right is not None:
                    temp.append(i.right)
            if len(temp) > 0:
                t.append(temp[-1].val)
            s = temp
        return t










