raw = open("input.txt")
class line:
    def __init__(self, line):
        self.name=line.split(" ")[0]
        self.weight=line[line.index("(")+1:line.index(")")]
        if line.find(">")!=-1:
            self.roots=line[line.find(">")+2:].split(", ")
        else:
            self.roots=None
x=[line(i.strip()) for i in raw.readlines()]
y=[]
for i in x:
    if i.roots == None:
        continue
    else:
        for root in i.roots:
            y.append(root)
for i in x:
    if i.name in y:
        continue
    else:
        print(i.name)
