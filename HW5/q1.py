
class node(object):

    def __init__(self, name, parent=None):
        self.name = name
        if parent is not None:
            self.p = parent
        else:
            self.p = self

    def __repr__(self):
        return str(self.name)

def find_set(x):
    """non-recursive method to find_set using previously implemented node objects"""
    ret = x
    while ret is not ret.p:
        ret = ret.p
    while x is not ret:
        temp = x.p
        x.p = ret
        x = temp
    return ret, list

x = node('x')
y = node('y', x)
z = node('z')
a = node('a', z)

print x, ':', find_set(x)
print y, ':', find_set(y)
print z, ':', find_set(z)
print a, ':', find_set(a)
print """>>> z.p = y"""
z.p = y
print z, ':', find_set(z)
print a, ':', find_set(a)
print """>>> a.p = a"""
a.p = a
print a, ':', find_set(a)
