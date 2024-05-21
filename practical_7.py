# Write a Program to accept a directed graph G and compute the in-degree and out degree of each vertex.


def compute_degrees(graph):
    in_degree = {}
    out_degree = {}

    # Initialize in-degree and out-degree dictionaries
    for vertex in graph:
        in_degree[vertex] = 0
        out_degree[vertex] = len(graph[vertex])

    # Compute in-degree
    for vertex in graph:
        for neighbor in graph[vertex]:
            in_degree[neighbor] += 1

    return in_degree, out_degree

# Example directed graph represented as a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A', 'D'],
    'D': ['B']
}

in_degree, out_degree = compute_degrees(graph)

print("Vertex\tIn-Degree\tOut-Degree")

for vertex in graph:
    print(f"{vertex}\t{in_degree[vertex]}\t\t{out_degree[vertex]}")



############### You can use this code as well


# def InOutDegree(adjList, n): 
     
#     _in = [0] * n 
#     out = [0] * n
 
#     for i in range(0, len(graph)): 
 
#         List = graph[i] 
#         out[i] = len(List) 
#         for j in range(0, len(List)):  
#             _in[List[j]] += 1
 
#     print("Vertex\tIn\tOut") 
#     for k in range(0, n): 
#         print(str(k) + "\t" + str(_in[k]) + "\t" + str(out[k]))
        

# n = int(input("Enter the lenght of the graph: "))
# graph=[]

# for i in range(n):
#     n1=int(input("Enter vertices connected: "))
#     l1=[]
#     for j in range(n1):
#         n=int(input("Enter number: "))
#         l1.append(n)
#     graph.append(l1)
# n = len(graph)
# InOutDegree(graph,n)

