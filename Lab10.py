#1.	Написати програму для пошуку найкоротшого шляху з кожної вершини до усіх інших вершин:
INF = float('inf')

def floyd_warshall(graph, vertices):
    num_vertices = len(vertices)
    distances = {vertex: {vertex: INF for vertex in vertices} for vertex in vertices}

    for vertex in vertices:
        distances[vertex][vertex] = 0

    for (i, j) in graph:
        distances[i][j] = graph[(i, j)]

    for k in vertices:
        for i in vertices:
            for j in vertices:
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances

def print_solution(distances):
    vertices = list(distances.keys())
    print("Матриця найкоротших відстаней між усіма парами вершин:")
    for i in vertices:
        for j in vertices:
            if distances[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distances[i][j], end=" ")
        print()

def main():

    graph = {
        ('a', 'b'): 1,
        ('b', 'd'): 5,
        ('b', 'c'): 2,
        ('b', 'z'): 7,
        ('c', 'a'): 2,
        ('c', 'e'): 4,
        ('c', 'd'): 1,
        ('d', 'z'): 1,
        ('e', 'c'): 3,
        ('z', 'e'): 1     
     

    }
    
    vertices = ['a', 'b', 'c', 'd', 'e', 'z']  

    distances = floyd_warshall(graph, vertices)
    

    print_solution(distances)

main()
