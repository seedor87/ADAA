from pprint import pprint

"""
src
http://blog.jupo.org/2012/04/06/topological-sorting-acyclic-directed-graphs/
"""

def topolgical_sort(graph_unsorted):
    """
    Repeatedly go through all of the nodes in the graph, moving each of
    the nodes that has all its edges resolved, onto a sequence that
    forms our sorted graph. A node has all of its edges resolved and
    can be moved once all the nodes its edges point to, have been moved
    from the unsorted graph onto the sorted one.
    """

    # This is the list we'll return, that stores each node/edges pair
    # in topological order.
    graph_sorted = []

    # Convert the unsorted graph into a hash table. This gives us
    # constant-time lookup for checking if edges are unresolved, and
    # for removing nodes from the unsorted graph.
    graph_unsorted = dict(graph_unsorted)

    # Run until the unsorted graph is empty.
    while graph_unsorted:

        # Go through each of the node/edges pairs in the unsorted
        # graph. If a set of edges doesn't contain any nodes that
        # haven't been resolved, that is, that are still in the
        # unsorted graph, remove the pair from the unsorted graph,
        # and append it to the sorted graph. Note here that by using
        # using the items() method for iterating, a copy of the
        # unsorted graph is used, allowing us to modify the unsorted
        # graph as we move through it. We also keep a flag for
        # checking that that graph is acyclic, which is true if any
        # nodes are resolved during each pass through the graph. If
        # not, we need to bail out as the graph therefore can't be
        # sorted.
        acyclic = False
        for node, edges in graph_unsorted.items():
            for edge in edges:
                if edge in graph_unsorted:
                    break
            else:
                acyclic = True
                del graph_unsorted[node]
                graph_sorted.append((node, edges))

        if not acyclic:
            # Uh oh, we've passed through all the unsorted nodes and
            # weren't able to resolve any of them, which means there
            # are nodes with cyclic edges that will never be resolved,
            # so we bail out with an error.
            raise RuntimeError("A cyclic dependency occurred")

    return graph_sorted

debug = 0

if debug:
    g = [('a', ['b','c']),
         ('b', ['d','e']),
         ('d', ['e']),
         ('f', ['g', 'h', 'a']),
         ('b', ['g'])]
    print topolgical_sort(g)

    g = [(2, []),
          (5, [11]),
          (11, [2, 9, 10]),
          (7, [11, 8]),
          (9, []),
          (10, []),
          (8, [9]),
          (3, [10, 8])]
    print topolgical_sort(g)

    g = [(2, [5]),  # NOTE addition of edge to node 5, creating cycle 2 -> 5 -> 11 -> 2
          (5, [11]),
          (11, [2, 9, 10]),
          (7, [11, 8]),
          (9, []),
          (10, []),
          (8, [9]),
          (3, [10, 8])]
    try:
        print topolgical_sort(g)
    except Exception as e:
        print str(e)
else:
    g = [('m', ['r', 'q', 'x']),
         ('t', []),
         ('q', ['t']),
         ('u', ['t']),
         ('x', []),
         ('n', ['q', 'u']),
         ('r', ['u', 'y']),
         ('o', ['r', 'v', 's']),
         ('v', ['x', 'w']),
         ('y', ['v']),
         ('s', ['r']),
         ('p', ['o', 's', 'z']),
         ('w', ['z']),
         ('z', [])]
    pprint(topolgical_sort(g))