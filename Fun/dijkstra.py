import sys
INF = sys.maxint
def initialize(graph, source):
    d = {}
    p = {}
    for node in graph:
        d[node] = INF
        p[node] = None
    d[source] = 0
    return d, p

def relax(node, neighbour, graph, d, p):
    if d[neighbour] > d[node] + graph[node][neighbour]:
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
            print "\t%s, %s, %s, %s" % (u, v, d_, p_) # results to table
        print 's:', S
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

def print_path(p, curr):
    if curr is None:
        return 0
    print_path(p, p[curr])
    print curr

def test():

    # graph = {
    #     's': {'t': 3, 'y': 5},
    #     't': {'x': 6, 'y': 2},
    #     'y': {'t': 1, 'z': 6, 'x': 4},
    #     'x': {'z': 2},
    #     'z': {'s': 3, 'x':7}
    # }
    #
    # print dijkstra(graph, 's')
    # print '-' * 100
    # print dijkstra(graph, 'z')

    graph = {
        'u': {'x': 5, 'w': 3, 'v': 7},
        'x': {'u': 5, 'w': 4, 'y': 7, 'z': 9},
        'w': {'u': 3, 'x': 4, 'v': 3, 'y': 8},
        'v': {'u': 7, 'w': 3, 'y': 4},
        'y': {'x': 7, 'w': 8, 'v': 4, 'z': 2},
        'z': {'x': 9, 'y': 2}
    }

    d, p = dijkstra(graph, 'u')
    print d, p
    print_path(p, 'z')
    print '-' * 100
    d, p = dijkstra(graph, 'z')
    print d, p
    print_path(p, 'u')


if __name__ == '__main__': test()