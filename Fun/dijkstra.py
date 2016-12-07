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
    Q = [(b,a) for a, b in d.items()]   # organize Q by (weight of vectors, node) pairs
    while Q:
        # print 'Q:', Q
        u = extract_min(Q)
        S += u
        for u, v in adj_list(graph, u):
            d_, p_ = relax(u, v, graph, d, p)
            print "%s, %s, %s, %s" % (u, v, d_, p_) # results to table
            print 'D:', d
            print 'P:', p
    return d, p

def adj_list(graph, u):
    ret = []
    for v in graph[u].keys():
        ret.append((u, v))
    return ret

def extract_min(list):
    heapify(list)
    return list.pop(0)[1]

def heapify(List):
    for root in xrange(len(List)//2-1, -1, -1):
        rootVal = List[root]
        child = 2*root+1
        while child < len(List):
            if child+1 < len(List) and List[child] > List[child+1]:
                child += 1
            if rootVal <= List[child]:
                break
            List[child], List[(child - 1) // 2] = List[(child - 1) // 2], List[child]
            child = child *2 + 1

def test():

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


if __name__ == '__main__': test()