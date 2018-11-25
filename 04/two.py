from collections import Counter
raw = open("input.txt")
db=[]
count=0
"""
for passphrase in raw.readlines():
  currentValid=True
  for i in Counter(passphrase.strip().replace("\n", "").split()).most_common():
    if i[1] != 1:
      currentValid=False
      continue
  if currentValid:
    count+=1
print(count)
"""
def sortWord(word):
    print("".join(sorted(word)))
sortWord("john")
