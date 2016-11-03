
class Set(list):

    def __init__(self, id):
        self.id = id
        self.p = self
        self.rank = 0

    def set_p(self, p):
        self.p = p

    def set_rank(self, rank):
        self.rank = rank

    def __repr__(self):
        if self.p == self:
            return "p: %s\tr: %s" % (self.id, self.rank)
        else:
            return "p: %s\tr: %s" % (self.p, self.rank)


def Union(x, y):

    Link(Find_Set(x), Find_Set(y))

def Link(x, y):

    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1

def Find_Set(x):

    if x != x.p:
        x.p = Find_Set(x.p)

    return x.p

x = Set('x')
y = Set('y')
z = Set('z')
print x
print y
print z
Find_Set(x)
Find_Set(y)
Find_Set(z)
print x
print y
print z
Union(x, y)
Union(z, y)
print x
print y
print z