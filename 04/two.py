from collections import Counter
raw = open("input.txt")
db=[]
count=0

def sortWord(word):
    return "".join(sorted(word))


for passphrase in raw.readlines():
  currentValid=True
  passphrase=passphrase.strip().replace("\n", "").split()
  for n,i in enumerate(passphrase):
      passphrase[n]=sortWord(i)
  for i in Counter(passphrase).most_common():
    if i[1] != 1:
      currentValid=False
      continue
  if currentValid:
    count+=1

print(count)
