import node as n
import edge as e
import graph as g

input = open("input_file.txt", "r")
output = open("output_file.txt", "w")

nodes = []
edges = []

first_line = input.readline().split()
num = int(first_line[0])
m = int(first_line[1])

second_line = input.readline().split()
for x in range(num - 1):
    nodes.append(n.Node(x + 1, second_line[x]))
    
third_line = input.readline().split()
rocket = third_line[0]
lucky = third_line[1]

for line in input.readlines():
    line = line.split()
    edges.append(e.Edge(line[0], line[1], line[2]))

input.close()
output.close()

graph = g.Graph(nodes, edges)

for node in graph.nodes:
    print(node.num, node.color)

for edge in graph.edges:
    print(edge.start, edge.end, edge.color)
