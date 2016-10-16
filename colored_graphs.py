colors_of_graphs = {}


def picking_color(graph_dict, graph, color):
    for graph in graph_dict.get(graph):
        color_of_neighbor = colors_of_graphs.get(graph)
        if color_of_neighbor == color:
            return False
    return True


def get_color_for_graph(graphs, graph, colors):
    for color in colors:
        if picking_color(graphs, graph, color):
            return color


def colored_graphs(graphs, colors):  # Input is
    for graph in graphs:
        colors_of_graphs[graph] = get_color_for_graph(graphs, graph, colors)
        return colors_of_graphs


def call_colored_graphs(graphs, colors):  # Input is
    for graph in graphs:
        colors_of_graphs[graph] = get_color_for_graph(graphs, graph, colors)
    for graph in graphs:
        print("Graph: " + str(graph) + '\n' +
              "Color: " + colors_of_graphs[graph])
# print(call_colored_graphs(graph_dict, colors))
