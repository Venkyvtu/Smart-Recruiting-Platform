x=int(input())
l=list(map(int,input().split()))
l.sort()
for i in range(1):
    for j in range(1,x):
        if sum(l[i:j])==sum(l[j:]):
            print("TRUE")
            break
    else:
        print("FALSE")
