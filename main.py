import networkx as nx
import matplotlib as plt

graph = nx.Graph()

input = open("input_file.txt", "r")
output = open("output_file.txt", "w")

first_line = input.readline().split()
graph.add_nodes([0, first_line[0]])

for line in input.readlines():
    line = line.split()
    graph.add_edge(line[0], line[1])

input.close()
output.close()

print(graph.number_of_nodes())
print(graph.number_of_edges())
