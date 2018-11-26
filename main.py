import networkx as nx
import matplotlib as plt

graph = nx.Graph()

input = open("input_file.txt", "r")
output = open("output_file.txt", "w")

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
output.close()

G = nx.petersen_graph()

plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.subplot(122)

nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
