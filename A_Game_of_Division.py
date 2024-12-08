t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    ls= list(map(int,input().split()))
    count=0

    for i in range(len(ls)):
        for j in range(len(ls)):
            if i != j and abs(ls[i] - ls[j]) != 0:
                a=(i + 1)
    print(i)
                