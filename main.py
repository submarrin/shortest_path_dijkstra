def read_graph():
    file_in = open("file_in.txt", 'r')
    n = int(file_in.readline())
    graph_matrix = [None] * n
    for i in range(n):
        graph_matrix[i] = [None] * n
    for i in range(n):
        line = file_in.readline().split() #array
        # print(pairs)
        for j in range(n):
            graph_matrix[i][j] = int(line[j])
    start = int(file_in.readline())
    finish = int(file_in.readline())
    file_in.close()
    return graph_matrix, int(start) - 1, int(finish) - 1


def find_shortest_path(matr, start, finish):
    n = len(matr)
    previous = [None]*n
    set_not_visited = [item for item in range(n)]
    final_distance = [32767]*n
    final_distance[start] = 0
    set_not_visited.remove(start)
    for vertex in set_not_visited:
        final_distance[vertex] = matr[start][vertex]
        previous[vertex] = start
    for i in range(n-1):
        max_distance_from_not_visited = -1
        for vertex in set_not_visited:
            if final_distance[vertex] > max_distance_from_not_visited:
                max_distance_from_not_visited = final_distance[vertex]
        vertex_with_max_distance = final_distance.index(max_distance_from_not_visited)
        set_not_visited.remove(vertex_with_max_distance)
        for vertex in set_not_visited:
            if final_distance[vertex_with_max_distance] + matr[vertex_with_max_distance][vertex] > final_distance[vertex]:
                final_distance[vertex] = final_distance[vertex_with_max_distance] + matr[vertex_with_max_distance][vertex]
                previous[vertex] = vertex_with_max_distance
    return 0


if __name__ == "__main__":
    matr, start, finish = read_graph()
    print(find_shortest_path(matr, start, finish))
    # don't forget to add 1 to all the vertices in final result
    pass

