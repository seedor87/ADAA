import sys

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

def dijkstra(graph, source):
    d, p = initialize(graph, source)
    print d, p
    S = []
    Q = ['s', 't', 'x', 'y', 'z']
    while Q:
        Q, u = extract_min(Q)
        S += u
        for u, v in adj_list(graph, u):
            d_, p_ = relax(u, v, graph, d, p)
            print "%s, %s, %s, %s" % (u, v, d_, p_)
    return d, p

def adj_list(graph, u):
    ret = []
    for v in graph[u].keys():
        ret.append((u, v))
    return ret

def extract_min(list):
    if not list:
        raise Exception("Empty List")
    _min = min(list)
    list.pop(list.index(_min))
    return list, _min

def test2():

    graph = {
        's': {'t': 3, 'y': 5},
        't': {'x': 6, 'y': 2},
        'y': {'t': 1, 'z': 6, 'x': 4},
        'x': {'z': 2},
        'z': {'s': 3, 'x':7}
    }

    print dijkstra(graph, 's')
    print '-' * 100
    print dijkstra(graph, 'z')


if __name__ == '__main__': test2()