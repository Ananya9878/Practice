def create(tree, root, low, high, l):
    if low == high:
        tree[root - 1] = l[low - 1]
        return tree[root - 1]
    mid = (low + high) // 2
    left = 2 * root
    right = 2 * root + 1
    a = create(tree, left, low, mid, l)
    b = create(tree, right, mid + 1, high, l)
    tree[root - 1] = a + b

    return tree[root - 1]

def update(tree,root,l,h,idx,value):
    if l == idx and h == idx:
        tree[root-1] = value
        return value
    left = 2*root
    right = 2*root+1
    mid = (l+h)//2
    if idx>mid:
        a=update(tree,right,mid+1,h,idx,value)
    else:
        b=update(tree,left,l,mid,idx,value)

    tree[root-1] = tree[left-1]+tree[right-1]

def query(tree,root,low,high,l,r):
    if l == low and r == high:
        return tree[root-1]
    elif r<low or l>high:
        return 0
    elif l>=low and r<=high:
        mid = (low+high)//2
        left = 2*root
        right = 2*root+1
        a = query(tree,left,low,mid,l,min(r,mid))
        b = query(tree,right,mid+1,high,max(l,mid+1),r)
        return a+b
    else:
        return 0

def main():
    # l = [1, 2, 3, 4, 5,6,7,8]
    l = list(map(int,input().split()))
    n = len(l)
    t = [-1]*(n*2)
    create(t,1,1,8,l)
    print(t)
    print("1. Update")
    print("2 Query")
    while 1:
        option = int(input("enter options:"))
        if option == 1:
            idx,value = map(int,input().split())
            update(t,1,1,n,idx,value)
            print(t)
        elif option == 2:
            l,r = map(int,input().split())
            a=query(t,1,1,n,l,r)
            print(a)
        else:
            break

main()