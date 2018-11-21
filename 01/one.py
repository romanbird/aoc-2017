x=str(open("input.txt", "r").readlines())
last_digit=x[-1]
count=0
for i in x:
  if i == last_digit:
    count+=int(i)
  last_digit=i
print(count)
