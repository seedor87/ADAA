import sys

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



graph = {0 : {1:6, 2:8},
         1 : {4:11},
         2 : {3:9},
         3 : {},
         4 : {5:3},
         5 : {2:7, 3:4}}

dist, pred = Floyd_Warshall(graph)
print "Predecessors in shortest path:"
for v in pred: print "%s: %s&" % (v, pred[v])
print "Shortest distance from each vertex:"
for v in dist: print "%s: %s" % (v, dist[v])

graph = {0 : {0:0, 1:1, 2:4, 3:10, 4:16, 5:5, 6:20},
         1 : {0:6, 1:0, 2:2, 3:14, 4:19, 5:2, 6:15},
         2 : {0:11, 1:13, 2:0, 3:2, 4:3, 5:17, 6:5},
         3 : {0:4, 1:22, 2:15, 3:0, 4:1, 5:18, 6:12},
         4 : {0:21, 1:3, 2:10, 3:5, 4:0, 5:10, 6:21},
         5 : {0:1, 1:20, 2:15, 3:2, 4:6, 5:0, 6:17},
         6 : {0:18, 1:3, 2:13, 3:8, 4:11, 5:2, 6:0}}

# graph = [[0, 1, 4, 10, 16, 5, 20],
#          [6, 0, 2, 14, 19, 2, 15],
#          [11, 13, 0, 2, 3, 17, 5,],
#          [4, 22, 15, 0, 1, 18, 12,],
#          [21, 3, 10, 5, 0, 10, 21],
#          [1, 20, 15, 2, 6, 0, 17],
#          [18, 3, 13, 8, 11, 2, 0]]

dist, pred = Floyd_Warshall(graph)
print "Predecessors in shortest path:"
for v in pred: print "%s: %s&" % (v, pred[v])
print "Shortest distance from each vertex:"
for v in dist: print "%s: %s" % (v, dist[v])