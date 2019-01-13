#selection sort

def SelectionSort(l):
    for start in range(len(l)):
        minpos=start
        for i in range(start,len(l)):
            if l[i]<l[minpos]:
                minpos=i
        (l[start],l[minpos])=(l[minpos],l[start])

l=[]
n=int(input("Size of list::"))
for i in range(0,n):
    x=int(input("Enter element::"))
    l.insert(i,x)
SelectionSort(l)
print("Sorted list",l)
