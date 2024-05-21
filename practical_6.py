# Write a Program to check if a given graph is a complete graph. Represent the graph using the Adjacency Matrix representation.

########## use any of the code

def complete_graph(adj_matrix):
    
    n = len(adj_matrix)
    
    for i in range(n):
        for j in range(i+1, n):
            if adj_matrix[i][j] == 0:
                return False
    return True

n = int(input("Enter the number of vertices in the graph: "))

print("Enter the adjacency matrix row by row (separate elements by space):")
adj_matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

if complete_graph(adj_matrix):
    print("The given graph is a complete graph.")
else:
    print("The given graph is not a complete graph.")





# def is_complete_graph(adj_matrix):
#     n = len(adj_matrix)
    
#     for i in range(n):
#         for j in range(n):
#             if i != j:
#                 if adj_matrix[i][j] != 1:
#                     return False
#             else:
#                 if adj_matrix[i][j] != 0:
#                     return False
                    
#     return True

# adj_matrix_complete = [
#     [0, 1, 1, 1],
#     [1, 0, 1, 1],
#     [1, 1, 0, 1],
#     [1, 1, 1, 0]
# ]

# print(is_complete_graph(adj_matrix_complete))  # Output: True

# adj_matrix_incomplete = [
#     [0, 1, 1, 0],
#     [1, 0, 1, 1],
#     [1, 1, 0, 0],
#     [0, 1, 0, 0]
# ]

# print(is_complete_graph(adj_matrix_incomplete))  # Output: False
