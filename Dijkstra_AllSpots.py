import sys
sys.setrecursionlimit(10000)

# Function to find minimum distance
def min_distance(distances, visited, n):
    min_dist = float('inf')
    min_index = -1
    for v in range(n):
        if not visited[v] and distances[v] < min_dist:
            min_dist = distances[v]
            min_index = v
    return min_index

# Fucntion to explore all paths to ensure each spot visited at least once. (Backtracking: Traverse not visited spots, select the shortest among all possible paths and store in cost to achieve hamiltonian path.)
def Visit_AllSpots(graph, current, unvisited, path, n, total_cost, all_paths, min_cost, destination, max_depth=1000):
    if len(path) > max_depth:
        return
        
    if len(unvisited) == 0 and current == destination:
        compressed_path = []
        for i in range(len(path)):
            if not compressed_path or compressed_path[-1] != path[i]:
                compressed_path.append(path[i])
                
        if total_cost < min_cost[0]:
            min_cost[0] = total_cost
            all_paths.clear()
            all_paths.append(compressed_path[:])
        elif total_cost == min_cost[0]:
            all_paths.append(compressed_path[:])
        return

    for neighbor in range(n):
        if graph[current][neighbor] == float('inf'):
            continue
            
        if path and neighbor == current:
            continue
            
        new_total_cost = total_cost + graph[current][neighbor]
        
        if new_total_cost >= min_cost[0]:
            continue
            
        path.append(neighbor)
        neighbor_was_unvisited = neighbor in unvisited
        if neighbor_was_unvisited:
            unvisited.remove(neighbor)
        
        Visit_AllSpots(graph, neighbor, unvisited, path, n, new_total_cost, all_paths, min_cost, destination, max_depth)
        
        path.pop()  # Backtracking
        if neighbor_was_unvisited:
            unvisited.add(neighbor)

# Dijkstra's Algorithm visiting all spots at least once (Shortest Path)
def dijkstra_AllSpots(graph, n, source, destination):
    unvisited = set(range(n))
    unvisited.remove(source)
    min_cost = [float('inf')]
    all_paths = []
    
    Visit_AllSpots(graph, source, unvisited, [source], n, 0, all_paths, min_cost, destination)
    
    # Display Results
    if min_cost[0] == float('inf'):
        print("No valid path exists.")
    else:
        print(f"\nShortest distance from Spot{source + 1} to Spot{destination + 1} "
              f"visiting all spots: {min_cost[0]}")
        print("\nOptimal Path:")
        for path in all_paths:
            print(" -> ".join(f"Spot{p + 1}" for p in path))

# Inputs
def get_graph_input():
    while True:
        try:
            m = int(input("Enter the number of spots: "))
            if m <= 0:
                print("Invalid input.")
                continue
            break
        except ValueError:
            print("Invalid input.")
    
    graph = [[float('inf')] * m for _ in range(m)]
    print("\nEnter the distances between the spots (enter 'inf' if there is no direct path):")
    
    for i in range(m):
        for j in range(m):
            if i != j:
                while True:
                    weight = input(f"Distance from Spot{i+1} to Spot{j+1}: ")
                    if weight.lower() == 'inf':
                        break
                    try:
                        val = int(weight)
                        if val < 0:
                            print("Invalid input.")
                            continue
                        graph[i][j] = val
                        break
                    except ValueError:
                        print("Invalid input.")
            else:
                graph[i][j] = 0
    return graph, m

def get_spot_input(prompt, m):
    while True:
        try:
            spot = int(input(prompt))
            if 1 <= spot <= m:
                return spot - 1
            print(f"Please enter a number between 1 and {m}.")
        except ValueError:
            print("Invalid input.")

# Main Function
if __name__ == "__main__":
    graph, m = get_graph_input()
    source = get_spot_input("\nEnter the source spot: ", m)
    destination = get_spot_input("Enter the destination spot: ", m)
    dijkstra_AllSpots(graph, m, source, destination)