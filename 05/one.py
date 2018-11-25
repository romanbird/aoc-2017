raw = open("input.txt")
db=[]
for i in raw.readlines():
    db.append(int(i.strip().replace("\n", "")))

#db=[0,3,0,1,-3] #expected 5
count=0
index=0
indexN=0
while True:
    try:
        indexN=db[index]
        index+=db[index]
        db[index-indexN]+=1
        count+=1
    except Exception as e:
        print(count)
        break
