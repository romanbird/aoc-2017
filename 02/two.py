import itertools
code = open("input.txt",'r')
rows = []
for i in code.readlines():
  i=i.strip().split("\t")
  rows.append([int(n) for n in i])

result=0

for row in rows:
    for number in itertools.combinations(row, 2):
        if number[0]%number[1]==0:
            result+=number[0]//number[1]
        elif number[1]%number[0]==0:
            result+=number[1]//number[0]
print(result)
