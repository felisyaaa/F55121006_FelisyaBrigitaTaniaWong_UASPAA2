import sys
import time
import heapq


def tsp(graph):
    start_time = time.time()

    num_cities = len(graph)
    visited = [False] * num_cities
    path = []
    min_cost = sys.maxsize

    def dfs(curr_city, count, cost):
        nonlocal min_cost

        if count == num_cities and graph[curr_city][0] > 0:
            min_cost = min(min_cost, cost + graph[curr_city][0])
            print(f"Iteration: {path + [0]} - Cost: {cost + graph[curr_city][0]}")

        for next_city in range(num_cities):
            if not visited[next_city] and graph[curr_city][next_city] > 0:
                visited[next_city] = True
                path.append(next_city)

                dfs(next_city, count + 1, cost + graph[curr_city][next_city])

                visited[next_city] = False
                path.pop()

    visited[0] = True
    path.append(0)
    dfs(0, 1, 0)

    end_time = time.time()
    execution_time = end_time - start_time

    return min_cost, execution_time


def dijkstra(graph, start):
    start_time = time.time()

    num_vertices = len(graph)
    distances = [sys.maxsize] * num_vertices
    distances[start] = 0
    pq = [(0, start)]  # Priority queue of (distance, vertex)

    while pq:
        curr_dist, curr_vertex = heapq.heappop(pq)

        if curr_dist > distances[curr_vertex]:
            continue

        for next_vertex in range(num_vertices):
            weight = graph[curr_vertex][next_vertex]
            if weight > 0:
                new_dist = curr_dist + weight
                if new_dist < distances[next_vertex]:
                    distances[next_vertex] = new_dist
                    heapq.heappush(pq, (new_dist, next_vertex))
                    print(f"Iteration: {curr_vertex} -> {next_vertex} - Distance: {new_dist}")

    end_time = time.time()
    execution_time = end_time - start_time

    return distances, execution_time


def main():
    graph = [
        [0, 8, 10, 0, 0, 0, 9, 12],
        [8, 0, 8, 10, 0, 0, 0, 0],
        [10, 8, 0, 8, 0, 0, 0, 0],
        [0, 10, 8, 0, 11, 0, 0, 11],
        [0, 0, 0, 11, 0, 6, 0, 0],
        [0, 0, 0, 0, 6, 0, 7, 0],
        [9, 0, 0, 0, 0, 7, 0, 12],
        [12, 0, 0, 11, 0, 0, 12, 0]
    ]

    print("Graph:")
    for row in graph:
        print(row)
    print()

    choice = input("1. TSP\n2. Dijkstra\nChoose algorithm: ")
    print()

    if choice == "1":
        tsp_cost, tsp_time = tsp(graph)
        print(f"Shortest Path Cost (TSP): {tsp_cost}")
        print(f"Execution Time (TSP): {tsp_time} seconds")

    elif choice == "2":
        start_vertex = int(input("Enter the start vertex: "))
        dijkstra_distances, dijkstra_time = dijkstra(graph, start_vertex)
        print("\nShortest Path Distances (Dijkstra):")
        for i, distance in enumerate(dijkstra_distances):
            print(f"Vertex {i}: {distance}")
        print(f"\nExecution Time (Dijkstra): {dijkstra_time} seconds")

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
1