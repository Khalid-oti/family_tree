import arabic_reshaper

class FamilyTree:
    def __init__(self):
        self.nil = Leaf(None)
        self.root = self.nil

    def add_root(self, leaf):
        if self.root == self.nil:
            self.root = leaf
        return

    def print_tree(self):
        lines = []
        if self.root != self.nil:
            self.arrange_tree(self.root, lines)
            return "\n".join(lines)
        return "empty tree :("
    
    def arrange_tree(self, leaf, lines, level=0):
        if leaf and leaf.name:
            lines.append("    " * level + "> " + leaf.name)
            if leaf.sons:
                for son in leaf.sons:
                    self.arrange_tree(son, lines, level+1)



class Leaf:
    def __init__(self, name):
        self.name = name #arabic_reshaper.reshape(name)[::-1]
        self.father = None
        self.sons = []

    def add_son(self, son):
        self.sons.append(son)
        son.father = self
    
    def get_fullname(self):
        full_name = ""
        current = self
        while current:
            full_name += f"{current.name} " #current.name + " " + full_name
            current = current.father
        return full_name


father = Leaf("mohammed")
son = Leaf("khalid")
father.add_son(son)

test_tree = FamilyTree()
test_tree.add_root(father)
print(test_tree.print_tree())
