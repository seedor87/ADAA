from pprint import pprint
import sys

inf = sys.maxint

def take_min(Q):
    # A (ascending or min) priority queue keeps element with
    # lowest priority on top. So pop function pops out the element with
    # lowest value. It can be implemented as sorted or unsorted array
    # (dictionary in this case) or as a tree (lowest priority element is
    # root of tree)
    lowest = inf
    keylowest = None
    for key in Q:
        if Q[key] < lowest:
            lowest = Q[key]
            keylowest = key
    del Q[keylowest]
    return keylowest

def prim(graph, root):
    pred = {} # pair {vertex: predecesor in MST}
    key = {}  # keep track of minimum weight for each vertex
    Q = {} # priority queue implemented as dictionary
    for v in graph:
        pred[v] = v
        key[v] = inf
    key[root] = 0
    for v in graph:
        Q[v] = key[v]
    while Q:
        u = take_min(Q)
        for v in graph[u]: # all neighbors of v
            if v in Q and graph[u][v] < key[v]:
                pred[v] = u
                key[v] = graph[u][v]
                Q[v] = graph[u][v]
    return pred

graph = {0 : {1:6, 2:8},
         1 : {4:11},
         2 : {3: 9},
         3 : {},
         4 : {5:3},
         5 : {2: 7, 3:4}}

pred = prim(graph, 0)
pprint(pred)
for v in pred: print "%s: %s" % (v, pred[v])

print '=' * 100

graph = {
        's': {'t': 6, 'y': 7},
        't': {'x': 5, 'y': 8, 'z': -4},
        'y': {'x': -3, 'z': 9},
        'x': {'t': -2},
        'z': {'s': 2, 'x': 4}
    }

pred = prim(graph, 's')
pprint(pred)
for v in pred: print "%s: %s" % (v, pred[v])