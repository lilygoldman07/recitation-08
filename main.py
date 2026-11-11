from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph

def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        ###TODO
        node = frontier.pop()
        for neighbor in graph[node]:
            # only add nodes we haven't seen yet, so no node is visited twice
            if neighbor not in result:
                result.add(neighbor)
                frontier.add(neighbor)
    return result

def connected(graph):
    ### TODO
    if len(graph) == 0:
        return True
    start = next(iter(graph))  # pick any node
    return len(reachable(graph, start)) == len(graph)

def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    ### TODO
    visited = set()
    count = 0
    for node in list(graph):
        # only call reachable on nodes not already in a found component
        if node not in visited:
            visited |= reachable(graph, node)
            count += 1
    return count
