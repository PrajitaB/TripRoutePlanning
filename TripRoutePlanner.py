import sys
sys.setrecursionlimit(10000)


# Knapsack Algorithm (Selection)
def knapsack(m, n, w, p, budget):

    # (w[i]/p[i]) ratio
    ratio = []
    for i in range(n):
        ratio.append([w[i] / p[i], w[i], p[i], i])

    # Sorting in descending order
    for i in range(n):
        for j in range(i + 1, n):
            if ratio[i][0] < ratio[j][0]:
                ratio[i], ratio[j] = ratio[j], ratio[i]

    S = [0] * n  # Solution Vector
    selected_spots = []
    prof = 0
    u = m  # u = remaining capacity (time)

    for i in range(n):
        duration = ratio[i][1]
        expense = ratio[i][2]
        index = ratio[i][3]

        if duration <= u and prof + expense <= budget:
            S[index] = 1
            selected_spots.append(index + 1)
            u -= duration
            prof += expense

    # Display
    print("\nSelected spots:")
    for spot in selected_spots:
        print(f"Spot {spot}")
 
    print(f"\nTotal expense: {prof}")
    print(f"Remaining budget: {budget - prof}")
    print(f"Total time: {m - u}")
    print(f"Remaining time: {u}")

    return selected_spots



# Recursive Function to explore all possible paths to ensure each spot is visited at least once (Backtracking: Traverse not visited spots, select the shortest among all possible paths and store in cost to achieve hamiltonian path.)
def Visit_AllSpots(graph, selected_spots, current, unvisited, path, n, total_cost, all_paths, min_cost, destination, max_depth=1000):
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
        
        Visit_AllSpots(graph, selected_spots, neighbor, unvisited, path, n, new_total_cost, all_paths, min_cost, destination, max_depth)
        
        path.pop()  # Backtracking
        if neighbor_was_unvisited:
            unvisited.add(neighbor)


# Modified Dijkstra's Algorithm visiting all selected spots at least once (Shortest Path)
def dijkstra_AllSpots(graph, n, source, destination, selected_spots):
    unvisited = set(range(n))
    unvisited.remove(source)
    min_cost = [float('inf')]
    all_paths = []
    
    Visit_AllSpots(graph, selected_spots, source, unvisited, [source], n, 0, all_paths, min_cost, destination)
    
    # Display Results
    if min_cost[0] == float('inf'):
        print("No valid path exists.")
    else:
        print(f"\nShortest distance from Spot {selected_spots[source]} to Spot {selected_spots[destination]} visiting all selected spots: {min_cost[0]}")
        print("\nOptimal Path:")
        for path in all_paths:
            print(" -> ".join(f"Spot {selected_spots[p]}" for p in path))


# Inputs for graph based on selected spots
def get_graph_input(selected_spots):
    m = len(selected_spots)
    graph = [[float('inf')] * m for _ in range(m)]
    print("\nEnter the distances between the selected spots (enter 'inf' if there is no direct path):")

    for i in range(m):
        for j in range(m):
            if i != j:
                while True:
                    try:
                        weight = input(f"Distance from Spot {selected_spots[i]} to Spot {selected_spots[j]}: ")
                        if weight.lower() == 'inf':
                            graph[i][j] = float('inf')
                            break
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
    return graph


# Inputs for source and destination from selected spots
def get_spot_input(prompt, selected_spots):
    while True:
        try:
            spot = int(input(prompt))
            if spot in selected_spots:
                return selected_spots.index(spot)  # Return index in selected_spots
            print(f"Please enter one of the selected spots: {', '.join(str(s) for s in selected_spots)}.")
        except ValueError:
            print("Invalid input.")



# Main Function
if __name__ == "__main__":
    
    # Inputs for Knapsack
    n = int(input("Enter the number of tourist spots: "))
    w = []  # Time
    p = []  # Expense
    for i in range(n):
        time = int(input(f"Enter the time required to visit spot {i + 1}: "))
        expense = int(input(f"Enter the expense to visit spot {i + 1}: "))
        w.append(time)
        p.append(expense)
    max_time = int(input("\nEnter the maximum time allowed: "))
    budget = int(input("Enter the maximum budget allowed: "))

    # Knapsack to get selected spots
    selected_spots = knapsack(max_time, n, w, p, budget)

    # Input for distances between selected
    graph = get_graph_input(selected_spots)
    source = get_spot_input("\nEnter the source spot: ", selected_spots)
    destination = get_spot_input("Enter the destination spot: ", selected_spots)

    # Dijkstra to get optimal path visiting all the selected spots
    dijkstra_AllSpots(graph, len(selected_spots), source, destination, selected_spots)