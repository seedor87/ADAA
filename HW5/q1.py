
class node(object):

    def __init__(self, name, parent=None):
        self.name = name
        if parent is not None:
            self.p = parent
        else:
            self.p = self

    def __repr__(self):
        return str(self.name)

def find_set(a):
    ret = a
    while ret.p is not ret:
        ret = ret.p
    _a = a
    next = a
    while next is not ret:
        next = _a.p
        _a = ret
    return ret

x = node('x')
y = node('y', x)
z = node('z', y)
a = node('a', z)
b = node('b')

print x, ':', find_set(x)
print y, ':', find_set(y)
print z, ':', find_set(z)
print a, ':', find_set(a)
print """>>> z.p = b"""
z.p = b
print a, ':', find_set(a)
print z, ':', find_set(z)
print """>>> a.p = y"""
a.p = y
print y, ':', find_set(y)
print a, ':', find_set(a)
print z, ':', find_set(z)

