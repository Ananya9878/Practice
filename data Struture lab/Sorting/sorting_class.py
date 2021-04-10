class List:
    def __init__(self,l):
        self.l = l

    def selection_sort(self):
        l=self.l
        for i in range(len(l)):
            m = i
            for j in range(m,len(l)):
                if l[m] > l[j]:
                    m = j
            l[m],l[i] = l[i],l[m]




    def bubble_sort(self):
        p = self.l
        for j in range(len(p)):
            for i in range(1,len(p)-j):
                if p[i] < p[i-1]:
                    p[i],p[i-1]=p[i-1],p[i]
        return


    def insertion_sort(self):
        # l=[2,3,4,10,12,3,1,6]
        l=self.l
        for i in range(len(l)):
            j=i
            while j>=0:
                if l[j]<l[i]:
                    break
                j-=1
            t=l.pop(i)
            l.insert(j+1,t)



    def print(self):
        print(*self.l)




def main():
    l=[1, 9, 3, 6, 7, 0, 4, 9, 5, 5]
    arr = List(l)
    print('1 selection sort')
    print('2 bubble sort')
    print('3 insertion sort')


    while 1:
        option = int(input('enter option'))
        if option == 1:
            arr.selection_sort()
            arr.print()
        elif option==2:
            arr.bubble_sort()
            arr.print()
        elif option==3:
            arr.insertion_sort()
            arr.print()
        else:
            break

if __name__ == '__main__':
    main()


