import sys
from sys import stdout

def Floyd_Warshall(G):
    dist = {}
    pred = {}
    for u in G:
        dist[u] = {}
        pred[u] = {}
        for v in G:
            dist[u][v] = sys.maxint
            pred[u][v] = -1
        dist[u][u] = 0
        for neighbor in G[u]:
            dist[u][neighbor] = G[u][neighbor]
            pred[u][neighbor] = u

    for t in G:
        for u in G:
            for v in G:
                newdist = dist[u][t] + dist[t][v]
                if newdist < dist[u][v]:
                    dist[u][v] = newdist
                    pred[u][v] = pred[t][v]

    return dist, pred

def print_path(P, i, j):
    if i == j:
        print '\t\t%s:\t%s' % (i, j)
    elif P[i][j] == 0:
        print "\t\tno path exists"
    else:
        print_path(P, i, P[i][j])
        print '\t\t%s:\t%s' % (i, j)

def print_input_graph(graph):
    print 'GRAPH:'
    keys = list(xrange(0,7))
    stdout.write('\t ')
    for i in keys:
        stdout.write("%d  " % i)
        stdout.flush()
    stdout.write("\n")
    for row in keys:
        stdout.write('%d:\t%s\n' % (row, [graph[row][w] for w in graph[row]]))
    stdout.flush()


graph = {
        'u': {'x': 5, 'w': 3, 'v': 7},
        'x': {'u': 5, 'w': 4, 'y': 7, 'z': 9},
        'w': {'u': 3, 'x': 4, 'v': 3, 'y': 8},
        'v': {'u': 7, 'w': 3, 'y': 4},
        'y': {'x': 7, 'w': 8, 'v': 4, 'z': 2},
        'z': {'x': 9, 'y': 2}
    }

print
print 'ANSWERS:'
dist, pred = Floyd_Warshall(graph)
print "Predecessors in shortest path:"
for v in pred: print "%s: %s" % (v, pred[v])
print "Shortest distance from each vertex:"
for v in dist: print "%s: %s" % (v, dist[v])

for key in pred.keys():
    print 'source:', key
    for _key in pred.keys():
        print '\tdestination:', _key
        print_path(pred, key, _key)

print '\n', '=' * 100, '\n'

graph = {0 : {0:0, 1:1, 2:4, 3:10, 4:16, 5:5, 6:20},
         1 : {0:6, 1:0, 2:2, 3:14, 4:19, 5:2, 6:15},
         2 : {0:11, 1:13, 2:0, 3:2, 4:3, 5:17, 6:5},
         3 : {0:4, 1:22, 2:15, 3:0, 4:1, 5:18, 6:12},
         4 : {0:21, 1:3, 2:10, 3:5, 4:0, 5:10, 6:21},
         5 : {0:1, 1:20, 2:15, 3:2, 4:6, 5:0, 6:17},
         6 : {0:18, 1:3, 2:13, 3:8, 4:11, 5:2, 6:0}}

print
print 'ANSWERS:'
dist, pred = Floyd_Warshall(graph)
print "Predecessors in shortest path:"
for v in pred: print "%s: %s" % (v, pred[v])
print "Shortest distance from each vertex:"
for v in dist: print "%s: %s" % (v, dist[v])

for key in pred.keys():
    print 'source:', key
    for _key in pred.keys():
        print '\tdestination:', _key
        print_path(pred, key, _key)