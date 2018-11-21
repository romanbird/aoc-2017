code = open("input.txt",'r')
rows = []
count=0
for i in code.readlines():
  i=i.strip().split("\t")
  rows.append([int(n) for n in i])
for i in rows:
    count+=(max(i)-min(i))
print(count)
