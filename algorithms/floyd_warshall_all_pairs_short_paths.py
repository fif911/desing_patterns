"""
https://www.programiz.com/dsa/floyd-warshall-algorithm
https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

INPUT:
       0    1    2    3
  0   {0,   5,   INF, 10}
  1   {INF, 0,   3,   INF}
  2   {INF, INF, 0,   1}
  3   {INF, INF, INF, 0}

which represents the following graph
          10
      (0)——-> (3)
       |      /|\
     5 |       |  1
       |       |
      \|/      |
      (1)——-> (2)
           3
Output: Shortest distance matrix
    0        5      8       9
    INF      0      3       4
    INF     INF     0       1
    INF     INF     INF     0

Vocab:
Vertex - вершина
Vertices -  вершини
"""

# Number of vertices in the graph
import copy
from pprint import pprint
from typing import List

V = 5

# Define infinity as the large
# enough value. This value will be
# used for vertices not connected to each other
INF = 99999

NAMES = ["Home", "Mall", "Park", "Gym", "Stadion"]


# Solves all pair shortest path
# via Floyd Warshall Algorithm

def calculate_row_source_via_intermediate_to_all_destinations(k: int, row_i: List, row_k: List):
    # k: id of intermediate
    # row_i: row that stores all distances from source to anywhere
    # row k store all distances from intermediate to anywhere
    # Node communications : 3n + 1
    # Node calculations: n

    # Impov: We can pass not only 1 row i but the set of rows distributed across machines
    # Then Deps: rows_i: List of Lists, upper bound, lower bound, row k
    # Node communications: GET: N(rows amount)/P(number of machines) * N(length of row) + N(row K)  + 2 int = N^2
    #                      SEND: P-1 * N ints
    #                      SEND: N(rows amount)/M(number of machines) ==> N^3
    # Node Calc: N/P * N  (scroll through each and calculate for each)

    row_calc = []
    for j in range(V):
        # If vertex k is on the shortest path from
        # i to j, then update the value of dist[i][j]
        temp = min(row_i[j],
                   # [i][k] - distance from source to intermediate
                   # [k][j] - distance from intermediate to destination
                   row_i[k] + row_k[j]
                   )
        row_calc.append(temp)

    return k, row_calc


def floydWarshall(graph):
    """ dist[][] will be the output matrix that will finally have the shortest distances
    between every pair of vertices """
    """ initializing the solution matrix same as input graph matrix OR we can say that the initial
    values of shortest distances are based on shortest paths considering no intermediate vertices """
    # pprint(graph)
    # dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
    dist = copy.deepcopy(graph)
    paths = [[0] * len(graph) for i in graph]
    # pprint(dist)
    """ Add all vertices one by one to the set of intermediate vertices.
     ---> Before start of an iteration, we have shortest distances between all pairs of vertices
     such that the shortest distances consider only the vertices in the set
    {0, 1, 2, .. k-1} as intermediate vertices.
      ----> After the end of a iteration, vertex no. k is added to the set of intermediate vertices and the
    set becomes {0, 1, 2, .. k}
    """
    for k in range(V):  # pick an intermediate node

        # pick all vertices as source one by one
        for i in range(V):
            row_id, row_calc = calculate_row_source_via_intermediate_to_all_destinations(k, row_i=dist[i],
                                                                                         row_k=dist[k])
            dist[i] = row_calc

            # Pick all vertices as destination for the above picked source
            # for j in range(V):
            #     # If vertex k is on the shortest path from
            #     # i to j, then update the value of dist[i][j]
            #     dist[i][j] = min(dist[i][j],
            #                      # [i][k] - distance from source to intermediate
            #                      # [k][j] - distance from intermediate to destination
            #                      dist[i][k] + dist[k][j]
            #                      )
    printSolution(dist)


# A utility function to print the solution
def printSolution(dist):
    print("Following matrix shows the shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if (dist[i][j] == INF):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == V - 1:
                print()


if __name__ == "__main__":
    """
                10
           (0)------->(3)
            |         /|\
          5 |          |
            |          | 1
           \|/         |
           (1)------->(2)
                3           """
    graph = [[0, 2, 8, 4, 6],
             [2, 0, 5, 1, INF],
             [8, INF, 0, INF, INF],
             [4, INF, INF, 0, 1],
             [6, INF, INF, 1, 0],
             ]
    # Function call
    floydWarshall(graph)
