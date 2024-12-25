# Define a large value for 'inf'
INF = float('inf')

# Function to initialize a 2D matrix for distances with both directions
def initialize_distance_matrix(selected_spots):
    n = len(selected_spots)
    distance_matrix = [[INF] * n for _ in range(n)]
    print("Enter the distances between spots (Enter 'inf' if no direct path):")
    
    for i in range(n):
        for j in range(n):
            if i != j:
                distance = input(f"Distance from {selected_spots[i]} to {selected_spots[j]}: ")
                if distance.lower() == 'inf':
                    distance_matrix[i][j] = INF
                else:
                    distance_matrix[i][j] = int(distance)
    
    return distance_matrix

# Function to get the index of a spot in selected_spots
def get_index(spot, selected_spots):
    return selected_spots.index(spot)

# TSP using dynamic programming with memoization, storing the path
def tsp_dp(mask, pos, dp, next_node, distance_matrix, selected_spots, destination_index):
    # If all spots are visited and we are at the destination, return 0 distance
    if mask == (1 << len(selected_spots)) - 1 and pos == destination_index:
        return 0

    # If already computed, return saved result
    if dp[mask][pos] != -1:
        return dp[mask][pos]

    min_distance = INF
    for next in range(len(selected_spots)):
        if mask & (1 << next) == 0 and distance_matrix[pos][next] != INF:
            # Recursive call
            new_distance = distance_matrix[pos][next] + tsp_dp(mask | (1 << next), next, dp, next_node, distance_matrix, selected_spots, destination_index)
            if new_distance < min_distance:
                min_distance = new_distance
                next_node[mask][pos] = next  # Store next node in path

    dp[mask][pos] = min_distance
    return min_distance

# Function to reconstruct the optimal path from stored information
def reconstruct_path(next_node, selected_spots, source_index, destination_index):
    path = [selected_spots[source_index]]
    mask = 1 << source_index
    pos = source_index

    while pos != destination_index:
        pos = next_node[mask][pos]
        if pos == -1:  # If there is no valid next step
            print("No valid path found.")
            return []
        path.append(selected_spots[pos])
        mask |= 1 << pos

    return path

# Function to find and print the optimal TSP path and distance
def find_optimal_path(selected_spots, source, destination):
    # Initialize distance matrix
    distance_matrix = initialize_distance_matrix(selected_spots)
    n = len(selected_spots)
    
    # Create DP and next_node tables with -1
    dp = [[-1] * n for _ in range(1 << n)]
    next_node = [[-1] * n for _ in range(1 << n)]
    
    # Get the index of source and destination
    source_index = get_index(source, selected_spots)
    destination_index = get_index(destination, selected_spots)
    
    # Find minimum distance
    optimal_distance = tsp_dp(1 << source_index, source_index, dp, next_node, distance_matrix, selected_spots, destination_index)
    
    # Retrieve the sequence of optimal path
    optimal_path = reconstruct_path(next_node, selected_spots, source_index, destination_index)

    # Display results
    print(f"Total distance covered: {optimal_distance}")
    print("Optimal path sequence:", " -> ".join(map(str, optimal_path)))

# Example usage:
selected_spots = [4, 3, 5, 2, 6]
source = int(input("Enter the source spot: "))
destination = int(input("Enter the destination spot: "))
find_optimal_path(selected_spots, source, destination)
