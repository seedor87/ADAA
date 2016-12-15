#script for Floyd Warshall Algorithm- All Pair Shortest Path
# http://codingjunkie.blogspot.com/2012/10/all-pair-shortest-path-floyd-warshall.html

import sys

INF = sys.maxint

def printSolution(distGraph):
    string = "inf"
    nodes =distGraph.keys()
    print ' ',
    for n in nodes:
        print "%3s"%(n),
    print " "
    for i in nodes:
        print"%s"%(i),
        for j in nodes:
            if distGraph[i][j] == INF:
                print "%s"%(string),
            else:
                print "%3s"%(distGraph[i][j]),
        print" "

def floydWarshall(graph):
    nodes = graph.keys()
    distance = {}
    for n in nodes:
        distance[n] = {}
        for k in nodes:
            distance[n][k] = graph[n][k]
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    printSolution(distance)

if __name__ == '__main__':
    graph = {'A':{'A':0,'B':6,'C':INF,'D':6,'E':7},
             'B':{'A':INF,'B':0,'C':5,'D':INF,'E':INF},
             'C':{'A':INF,'B':INF,'C':0,'D':9,'E':3},
             'D':{'A':INF,'B':INF,'C':9,'D':0,'E':7},
             'E':{'A':INF,'B':4,'C':INF,'D':INF,'E':0}
             }
    floydWarshall(graph)

    graph = {0 : {0:0, 1:1, 2:4, 3:10, 4:16, 5:5, 6:20},
         1 : {0:6, 1:0, 2:2, 3:14, 4:19, 5:2, 6:15},
         2 : {0:11, 1:13, 2:0, 3:2, 4:3, 5:17, 6:5},
         3 : {0:4, 1:22, 2:15, 3:0, 4:1, 5:18, 6:12},
         4 : {0:21, 1:3, 2:10, 3:5, 4:0, 5:10, 6:21},
         5 : {0:1, 1:20, 2:15, 3:2, 4:6, 5:0, 6:17},
         6 : {0:18, 1:3, 2:13, 3:8, 4:11, 5:2, 6:0}}
    floydWarshall(graph)