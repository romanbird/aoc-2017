import one
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
    if backlog.count(tuple(x)) == 2:
        break
    backlog.append(tuple(x))
print((len(backlog)+1)-one.main())
