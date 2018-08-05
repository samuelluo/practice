def shortest_path(start_node, end_node):
    # {node : distance}; distance from start_node to current_node
    paths = {start_node : ['A']}
    queue = [start_node]
    while len(queue) != 0:
        curr_node = queue.pop(0)
        # Check all connections of curr_node
        for node in graph[curr_node]:
            if node not in paths.keys():
                paths[node] = paths[curr_node] + [node]
                queue.append(node)
    return paths[end_node]

# --------------------------------------------------
graph = {'A' : ['B'],
         'B' : ['A', 'D', 'C'],
         'C' : ['B', 'D'],
         'D' : ['B', 'C']}

# Answer: 2 (A -> B -> D)
start_node = 'A'
end_node = 'D'
result = shortest_path(start_node, end_node)
print([result, len(result)-1])