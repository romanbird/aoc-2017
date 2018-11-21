x=str(open("input.txt", "r").readlines())
count=0
for n,i in enumerate(x):
  if x[n] == x[(n+(int(len(x)/2)))%len(x)]:
    count+=int(x[n])
print(count)
