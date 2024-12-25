# Function to find minimum distance
def min_distance(distances, visited, n):
    min_dist = float('inf')
    min_index = -1
    for v in range(n):
        if not visited[v] and distances[v] < min_dist:
            min_dist = distances[v]
            min_index = v
    return min_index
##############################################

# Dijkstra's Algorithm
def dijkstra(graph, n, source, destination):
    
    distances = [float('inf')] * n
    previous_nodes = [-1] * n
    distances[source] = 0
    visited = [False] * n
    
    for _ in range(n):
        u = min_distance(distances, visited, n)
        if u == -1:
            break
        visited[u] = True
        
        for v in range(n):
            if graph[u][v] != float('inf') and not visited[v]:
                new_dist = distances[u] + graph[u][v]
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    previous_nodes[v] = u

    # Shortest path
    path = []
    current = destination
    while current != -1:
        path.insert(0, current + 1) 
        current = previous_nodes[current]
    if distances[destination] == float('inf'):
        print("No path exists between the given source and destination.")
    else:
        print(f"Shortest distance from Spot{source + 1} to Spot{destination + 1}: {distances[destination]}")
        print("Optimal Path:", " -> ".join(f"Spot{p}" for p in path))


# Inputs
m = int(input("Enter the number of spots: "))
graph = [[float('inf')] * m for _ in range(m)]

print("Enter the distances between the spots (enter 'inf' if there is no direct path):")
for i in range(m):
    for j in range(m):
        if i != j:
            weight = input(f"Distance from Spot{i+1} to Spot{j+1}: ")
            if weight != 'inf':
                try:
                    graph[i][j] = int(weight)
                except ValueError:
                    print("Invalid input.")
                    graph[i][j] = float('inf')
        else:
            graph[i][j] = 0

source = int(input("Enter the source spot (1 to n): ")) - 1
destination = int(input("Enter the destination spot (1 to n): ")) - 1


dijkstra(graph, m, source, destination)