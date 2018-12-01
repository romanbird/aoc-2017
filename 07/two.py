raw = open("input2.txt")
nodes = dict()
class node:
    def __init__(self, node):
        self.name=node.split(" ")[0]
        self.weight=node[node.index("(")+1:node.index(")")]
        self.children = []
        if node.find(">")!=-1:
            children_names=node[node.find(">")+2:].split(", ")
            for child in children_names:
                self.children.append(nodes[child])

        else:
            self.children=None
    def find_weight(self):
        return self.weight + map(find_weight, self.children)


for i in raw.readlines():
    nodes[i.split(" ")[0]] = node(i)

print([i for i in nodes])
