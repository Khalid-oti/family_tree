import arabic_reshaper

class FamilyTree:
    def __init__(self):
        self.nil = Node(None)
        self.root = self.nil
        self.nodes = {}

    def add_node(self, node):
        if self.root == self.nil:
            if node.father:
                self.nodes[node.father.id] = node.father
                self.root = node.father
                self.nodes[node.id] = node
            else:
                self.nodes[node.id] = node
                self.root = node
        elif node.father:
            if node.father.id in self.nodes:
                self.nodes[node.id] = node
            else:
                return f"{node.father} does not exist"
        else:
            return "father not provided"
        for child in node.children:
            self.nodes[child.id] = child
    
    def delete_node(self, node):
        if len(node.children) > 1 or node.father:
            return f"cannot delete {node}"
        else:
            if self.root == node:
                node.children[0].father = None
                self.root = node.children[0]
                node.children = []
            if node.father:
                node.father.children.remove(node)
                node.father = None
            self.nodes.pop(node.id)
            node.name = None
            node.id = -1

    def print_tree(self):
        lines = []
        if self.root != self.nil:
            self.arrange_tree(self.root, lines)
            return "\n".join(lines)
        return "empty tree :("
    
    def arrange_tree(self, node, lines, level=0):
        if node.name:
            lines.append("    " * level + "> " + node.name)
            for child in node.children:
                self.arrange_tree(child, lines, level+1)



class Node:
    def __init__(self, name):
        self.name = arabic_reshaper.reshape(name)[::-1] if name else None
        self.father = None
        self.children = []
        self.id = sum(ord(char) for char in self.get_fullname()) if name else -1

    def add_children(self, children):
        for child in children:
            child_node = Node(child)
            self.children.append(child_node)
            child_node.father = self
    
    def add_father(self, father):
        if self.father:
            return
        father_node = Node(father)
        self.father = father_node
        father_node.children.append(self)
    
    def get_fullname(self):
        full_name = ""
        current = self
        while current:
            full_name = current.name + " " + full_name
            current = current.father
        return full_name



testtree = FamilyTree()
testnode = Node("عايض")

sons = ["منير", "محمد", "مهتصم", "مهند", "سعود", "عمر"]
testnode.add_children(sons)

testtree.add_node(testnode)
s2 = Node("عزيز")
testnode.add_children(["عزيز"])


print(testtree.print_tree())

print(Node(None).name)
