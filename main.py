import networkx as nx
import matplotlib as plt

graph = nx.Graph()

input = open("input_file.txt", "r")
output = open("output_file.txt", "w")

first_line = input.readline().split()
graph.add_nodes_from([1, first_line[0]])

second_line = input.readline().split()
for x in range(int(first_line[0])):
    graph[x + 1]['color'] = second_line[x]

for line in input.readlines():
    line = line.split()
    graph.add_edge(line[0], line[1])
    graph[line[0]][line[1]]['color'] = line[2]

input.close()
output.close()

graph.nodes.data()
graph.edges.data()
