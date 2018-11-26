x = [int(i) for i in open("input.txt").readlines()[0].split()]
#x = [0,2,7,0] # test input, expecting 5
backlog=[]
while True:
    maxx=max(x)
    location=x.index(maxx)
    x[location]=0
    i=0
    while i != maxx:
        x[(location+1+i)%len(x)]+=1
        i+=1
    if tuple(x) in backlog:
        break
    backlog.append(tuple(x))
print(x)
print(len(backlog)+1)
