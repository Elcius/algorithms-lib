from heapq import heappush, heappop


def shortest_path(graph, start):
    if start not in graph:
        return "Bad input!"
    # Create answer's list
    answer_list = [None] * len(graph)
    queue = [(0, start)]
    # Use heap queue to check the unvisited graphs
    while queue:
        path_len, v = heappop(queue)
        if answer_list[v] is None:
            answer_list[v] = path_len
            for weight, edge_len in graph[v].items():
                if answer_list[weight] is None:
                    heappush(queue, (path_len + edge_len, weight))
    return [0 if not x else x for x in answer_list]


def call_shortest_path(graph, start):
    sp = shortest_path(graph, start)
    x = 1
    print("Shortest distance from all graphs to Graph " + str(start) + ":")
    for x in range(len(sp)):
        if x == start:
            print("Graph " + str(x) + ": self")
        else:
            print("Graph " + str(x) + ": " + str(sp[x]))