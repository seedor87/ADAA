import sys
"""
The Bellman-Ford algorithm
Graph API:
    iter(graph) gives all nodes
    iter(graph[u]) gives neighbours of u
    graph[u][v] gives weight of edge (u, v)
"""

# Step 1: For each node prepare the destination and predecessor
def initialize(graph, source):
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    for node in graph:
        d[node] = sys.maxint # We start admitting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p

def relax(node, neighbour, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # Record this lower distance
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node
    return d[neighbour], p[neighbour]

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    print d, p
    for i in range(len(graph)-1): # Run this until is converges

        for u, v in edges(graph):
            d_, p_ = relax(u, v, graph, d, p)
            print "%s, %s, %s, %s" % (u, v, d_, p_) # Lets relax

    # Step 3: check for negative-weight cycles
    for u, v in edges(graph):
        print u, v, d[v] , ">", d[u] , "+", graph[u][v]
        assert d[v] <= d[u] + graph[u][v]

    return d, p

def edges(graph):
    ret = []
    for k, v in graph.iteritems():
        for _k in v.keys():
            ret.append((k, _k))
    return ret

def test():
    # graph = {
    #     'a': {'b': -1, 'c':  4},
    #     'b': {'c':  3, 'd':  2, 'e':  2},
    #     'c': {},
    #     'd': {'b':  1, 'c':  5},
    #     'e': {'d': -3}
    #     }
    #
    # d, p = bellman_ford(graph, 'a')
    # print d
    # print p

    graph = {
       's': {'t': 6, 'y': 7},
       't': {'x': 5, 'y': 8, 'z': -4},
       'y': {'x': -3, 'z': 9},
       'x': {'t': -2},
       'z': {'s': 2, 'x': 7}
    }

    d, p = bellman_ford(graph, 's')
    print d
    print p

    d, p = bellman_ford(graph, 'z')
    print d
    print p

    print "-" *(100)

    graph = {
        's': {'t': 6, 'y': 7},
        't': {'x': 5, 'y': 8, 'z': -4},
        'y': {'x': -3, 'z': 9},
        'x': {'t': -2},
        'z': {'s': 2, 'x': 4}
    }

    d, p = bellman_ford(graph, 'z')
    print d
    print p


if __name__ == '__main__': test()