def read_graph():
    file_in = open("file_in.txt", 'r')
    n = int(file_in.readline())
    graph_matrix = [None] * n
    for i in range(n):
        graph_matrix[i] = [None] * n
    for i in range(n):
        line = file_in.readline().split()  # array
        for j in range(n):
            graph_matrix[i][j] = int(line[j])
    start = int(file_in.readline())
    finish = int(file_in.readline())
    file_in.close()
    return graph_matrix, int(start) - 1, int(finish) - 1


def get_path_from_array_of_previous(array_of_previous, start, finish):
    path = []
    temporary_vertex = finish
    while temporary_vertex != -1:
        path.append(temporary_vertex)
        temporary_vertex = array_of_previous[temporary_vertex]
    return path


def find_vertex_with_min_distance_from_set_not_visited(set_not_visited, distance_array, min_distance):
    min_vertex = None
    for vertex in set_not_visited:
        if distance_array[vertex] < min_distance:
            min_distance = distance_array[vertex]
    for vertex in set_not_visited:
        if distance_array[vertex] == min_distance:
            min_vertex = vertex
    return min_vertex


def find_shortest_path(matr, start, finish):
    n = len(matr)
    previous = [None] * n
    set_not_visited = [item for item in range(n)]
    distance = [32767] * n
    distance[start] = 0
    set_not_visited.remove(start)
    previous[start] = -1
    print("set not visited: ", set_not_visited)
    for vertex in set_not_visited:
        distance[vertex] = matr[start][vertex]
        previous[vertex] = start
    for i in range(n - 1):
        print("i = ", i + 1)
        min_distance_from_not_visited = 32767
        vertex_with_min_distance = find_vertex_with_min_distance_from_set_not_visited(set_not_visited, distance,
                                                                                      min_distance_from_not_visited)
        set_not_visited.remove(vertex_with_min_distance)
        print("set not visited = ", set_not_visited)
        # finding min distance
        for vertex in set_not_visited:
            if distance[vertex_with_min_distance] * matr[vertex_with_min_distance][vertex] < distance[vertex] and \
                    matr[vertex_with_min_distance][vertex] != 32767:
                distance[vertex] = distance[vertex_with_min_distance] * matr[vertex_with_min_distance][vertex]
                previous[vertex] = vertex_with_min_distance
    print("array of final distance", distance)
    reversed_path = get_path_from_array_of_previous(previous, start, finish)
    path = []
    for vertex in reversed_path:
        vertex += 1
        path.append(vertex)
    path.reverse()
    print("path = ", path)
    return distance[finish]


if __name__ == "__main__":
    matr, start, finish = read_graph()
    print(find_shortest_path(matr, start, finish))
    # don't forget to add 1 to all the vertices in final result
    pass
