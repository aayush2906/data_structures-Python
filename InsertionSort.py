
def InsertionSort(seq):
    for sliceEnd in range(len(seq)):
        pos=sliceEnd
        while pos > 0 and seq[pos] < seq[pos-1]:
            (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
            pos=pos-1
seq=[]
n=int(input("Size of list::"))
for i in range(0,n):
    x=int(input("Enter element::"))
    seq.insert(i,x)
InsertionSort(seq)
print("Sorted list",seq)         
   
