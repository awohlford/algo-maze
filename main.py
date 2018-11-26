import networkx as nx
import node as n
import edge


graph = nx.Graph()

input = open("input_file.txt", "r")

first_line = input.readline().split()

second_line = input.readline().split()
for x in range(int(first_line[0]) - 1):
    graph.add_node((x + 1), color=second_line[x])
    
third_line = input.readline().split()
rocket = third_line[0]
lucky = third_line[1]

for line in input.readlines():
    line = line.split()
    graph.add_edge(line[0], line[1], color=line[2])

input.close()

print(list(nx.bfs_tree(graph,1).edges()))
