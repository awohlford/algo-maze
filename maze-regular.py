input = open("input_file.txt", "r")
output = open("output_file.txt", "w")

nodes = []
edges = []

first_line = input.readline().split()
n = int(first_line[0])
m = int(first_line[1])

second_line = input.readline().split()
for x in range(n - 1):
    nodes.append(Node(x + 1, second_line[x]))
    
third_line = input.readline().split()
rocket = third_line[0]
lucky = third_line[1]

for line in input.readlines():
    line = line.split()
    edges.append(line[0], line[1], line[2])

input.close()
output.close()

graph = Graph(nodes, edges)

print(nodes, edges)
