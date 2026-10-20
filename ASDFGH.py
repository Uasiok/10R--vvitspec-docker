#test
a=int(input())
sp=list(map(int,input().split()))
def qsort(sp):
    if(len(sp)<=1):
        return sp
    else:
        n=len(sp)//2
        pivot=sp[n]
        left=[]
        middle=[]
        right=[]
        for i in sp:
            if(i<pivot):
                left.append(i)
            elif(i==pivot):
                middle.append(i)
            else:
                right.append(i)
        return qsort(left)+middle+qsort(right)
print(*qsort(sp))
