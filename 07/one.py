raw = open("input2.txt")
class line:
    def __init__(self, line):
        self.name=line.split(" ")[0]
        self.number=line[line.index("(")+1:line.index(")")]
        if line.find(">")!=-1:
            self.roots=line[line.find(">")+2:].split(", ")
        else:
            self.roots=None
x=[line(i.strip()) for i in raw.readlines()]
for i in x:
    print(i.name)
