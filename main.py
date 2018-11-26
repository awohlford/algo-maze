import networkx as nx
import matplotlib as plt

graph = nx.Graph()

input = open("input_file.txt", "r")
output = open("output_file.txt", "w")

first_line = input.readline().split()

second_line = input.readline().split()
for x in range(int(first_line[0])):
    graph.add_node((x + 1), second_line[x])

for line in input.readlines():
    line = line.split()
    graph.add_edge(line[0], line[1])
    #graph[line[0]][line[1]]['color'] = line[2]

input.close()
output.close()

print(graph.nodes.data())
print(graph.edges.data())
