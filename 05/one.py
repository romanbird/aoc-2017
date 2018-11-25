raw = open("input.txt")
db=[]
for i in raw.readlines():
    db.append(int(i.strip().replace("\n", "")))
print(db)
