""" INPUT READER
raw = open("input.txt")
db=[]
for i in raw.readlines():
    db.append(int(i.strip().replace("\n", "")))
"""
db=[0,3,0,1,-3]
index=0
current=0
count=0
new=0
while True:
    try:
        print(db)
        current=db[index]
        new=db[index+current]
        db[current]+=1
        index+=db[index]


    except Exception as e:
        print(e)
        print(count)
        break
