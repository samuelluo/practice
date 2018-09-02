"""
Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
A 1 represents land and 0 represents water, so an island is a group of 1s that 
are neighboring and their perimeter is surrounded by water.

For example, this matrix has 4 islands:
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""

# ---------------------------------------------------------
def graph_islands_helper(graph, directions):
    # Set up
    unvisited = [(i, j)
                 for i in range(len(graph))
                 for j in range(len(graph[0]))
                 if graph[i][j] == 1]
    visited = []
    num_islands = 0

    # Breadth first search
    while len(unvisited) != 0:
        node = unvisited[0]    # unvisited tracks all nodes left
        num_islands += 1
        queue = [node]
        while len(queue) != 0:
            node = queue.pop(0)    # queue tracks current island
            visited.append(node)
            unvisited.pop(unvisited.index(node))
            for direction in directions:
                new_i = node[0] + direction[0]
                new_j = node[1] + direction[1]
                new_node = (new_i, new_j)
                if 0 <= new_i < len(graph) and \
                   0 <= new_j < len(graph[0]) and \
                   new_node not in visited and \
                   new_node not in queue and \
                   graph[new_i][new_j] == 1:
                    queue.append(new_node)

    # Return
    return num_islands

def graph_islands(graph):
    # Diagonal connections supported
    dir_8 = [(i, j)
             for i in [-1, 0, +1]
             for j in [-1, 0, +1]
             if (i, j) != (0, 0)]
    result_8 = graph_islands_helper(graph, dir_8)

    # Diagonal connections not supported
    dir_4 = [(i, j)
             for i in [-1, 0, +1]
             for j in [-1, 0, +1]
             if (i, j) != (0, 0) and abs(i) != abs(j)]
    result_4 = graph_islands_helper(graph, dir_4)

    # Return
    return (result_8, result_4)

# ---------------------------------------------------------
# Answer: (4, 4)
graph = [[1, 0, 0, 0, 0],
         [0, 0, 1, 1, 0],
         [0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 1, 0, 0, 1],
         [1, 1, 0, 0, 1]]
result = graph_islands(graph)
print(result)

# Answer: (5, 6)
graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]
result = graph_islands(graph)
print(result)

# Answer: (1, 5)
graph = [[1, 0, 0, 1],
         [0, 1, 1, 0],
         [0, 1, 1, 0],
         [1, 0, 0, 1]]
result = graph_islands(graph)
print(result)