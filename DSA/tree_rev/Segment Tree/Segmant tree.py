class Node:
    def __init__(self,data,range):
        self.data = data
        self.left = None
        self.right = None
        self.range = range

class segmentTree:
    def __init__(self,l):
        self.root = None
        self.create(l)


    def create(self,l):
        l = [Node(l[i],(i+1,i+1)) for i in range(len(l))]

        while len(l) != 1:
            temp = []
            while len(l) > 1:
                a, b = l.pop(0), l.pop(0)
                c_data = a.data+b.data
                c_range = (a.range[0],b.range[-1])
                c = Node(c_data,c_range)
                c.left = a
                c.right = b
                temp.append(c)
            temp += l
            l = temp

        self.root = l[0]


    def create1(self,l):
        tree = l[::]

        while len(l)!=1:
            temp = []
            # print(l)
            while len(l)>1:
                a,b = l.pop(0),l.pop(0)
                temp.append(a+b)
            l = temp
            tree = l+tree
        return tree

    def create2(self,tree,root,low,high,l):
        if low == high:
            tree[root-1] = l[low-1]
            return tree[root-1]
        mid = (low+high)//2
        left = 2*root
        right = 2*root+1
        a = self.create2(tree,left,low,mid,l)
        b = self.create2(tree,right,mid+1,high,l)
        tree[root-1]=a+b

        return tree[root-1]



    def update(self,tree,n,idx,value):
        new_idx = n-idx
        # print(new_idx)
        i = len(tree)-new_idx+1
        # print(i)
        tree[i-1] = value
        while i>1:
            parent = i//2
            left_child = 2*parent
            right_child = 2*parent+1
            tree[parent-1] = tree[left_child-1]+tree[right_child-1]
            # print(parent,left_child,right_child)
            i = parent

        return tree

    def update1(self,tree,root,l,h,idx,value):
        if l == idx and h == idx:
            tree[root-1] = value
            return value
        left = 2*root
        right = 2*root+1
        mid = (l+h)//2
        if idx>mid:
            a=self.update1(tree,right,mid+1,h,idx,value)
        else:
            b=self.update1(tree,left,l,mid,idx,value)

        tree[root-1] = tree[left-1]+tree[right-1]






    def query(self,tree,root,low,high,l,r):
        if l == low and r == high:
            return tree[root-1]
        elif r<low or l>high:
            return 0
        elif l>=low and r<=high:
            mid = (low+high)//2
            left = 2*root
            right = 2*root+1
            a = self.query(tree,left,low,mid,l,min(r,mid))
            b = self.query(tree,right,mid+1,high,max(l,mid+1),r)
            return a+b
        else:
            return 0

# mid = 4
# left = 2
# right = 3
# a = (1,4,1,2)
# b = (5,8,5,2)








    def display(self):
        s = [self.root]
        print(self.root.data)
        while len(s)>0:
            temp = []
            temp1 = []
            for i in s:
                if i.left is not None:
                    temp.append(i.left)
                    temp1.append((i.left.data,i.left.range))
                if i.right is not None:
                    temp.append(i.right)
                    temp1.append((i.right.data,i.right.range))

            s = temp
            print(temp1)



def main():
    l=[1,2,3,4,5]
    n = len(l)
    ST = segmentTree(l)
    # ST.display()
    # t=ST.create1(l)
    # print(t)
    # f=ST.query(t,1,1,8,3,8)
    # print(f)
    # ST.update1(t,1,1,8,5,10)
    # print(t)
    l = [1, 2, 3, 4, 5]
    t = [-1]*(n*2)
    ST.create2(t,1,1,5,l)
    print(t)


    # t = ST.update(t,n,4,10)
    # print(t)
if __name__ == '__main__':
    main()






