code = open("input.txt",'r')
rows = []
for i in code.readlines():
  i=i.strip().split("\t")
  rows.append([int(n) for n in i])
