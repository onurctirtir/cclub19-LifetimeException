from itertools import permutations


class DistancePath:
    def __init__(self, distance, path):
        """
        :type distance: float
        :type path: str
        """
        self.distance = distance
        self.path = path


class Graph:
    def __init__(self, n_foods):
        self.__n_foods = n_foods
        self.data = dict()

    def set_distancePath(self, o1, o2, distance_path):
        """
        :type distance_path: DistancePath
        """
        if o1 not in self.data.keys():
            self.data[o1] = dict()

        self.data[o1][o2] = distance_path

    def get_distancePath(self, o1, o2):
        if o1 not in self.data.keys() or o2 not in self.data[o1].keys():
            return False
        return self.data[o1][o2]


# run bfs on given board between coordinates (x1, y1) and (x2, y2)
# return shortest distance and path string
def run_bfs(board, x1, y1, x2, y2, visited):
    nrows = len(board)
    ncols = len(board[0])

    for i in range(nrows):
        for j in range(ncols):
            visited[i][j] = False

    queue = [(x1, y1)]
    visited[x1][y1] = DistancePath(distance=0, path='')

    while queue:
        x, y = queue[0]
        queue.pop(0)

        if x == x2 and y == y2:
            return visited[x2][y2]

        for cx, cy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if 0 <= cx < nrows and 0 <= cy < ncols:
                if board[cx][cy] not in ('-', '*') and cx != x2 and cy != y2:
                    continue

                if (board[cx][cy] == '*' and not visited[cx][cy]) or (cx == x2 and cy == y2):
                    visited[cx][cy] = DistancePath(distance=visited[x][y].distance, path=visited[x][y].path)

                    visited[cx][cy].distance += 1

                    if cx > x:
                        directory = 'S'
                    elif cx < x:
                        directory = 'N'
                    elif cy > y:
                        directory = 'E'
                    elif cy < y:
                        directory = 'W'

                    visited[cx][cy].path += directory

                    queue.append((cx, cy))

    return False


def main():
    m, n, k = map(int, input().split())

    board = [['' for _ in range(n)] for _ in range(m)]
    # use in run_bfs
    garbage_board = [[False for _ in range(n)] for _ in range(m)]

    foods_and_start_end = {}

    # save input board
    for i in range(m):
        line = input()

        for j in range(n):
            c = line[j]

            # simplify board
            if c in ('^', '-'):
                c = '-'

            # save object to board
            board[i][j] = c

            # save important object's location
            if c not in ('-', '*'):
                foods_and_start_end[c] = (i, j)

    # resolve relative distances, construct graph
    nfoods = len(foods_and_start_end.keys()) - 2

    graph = Graph(n_foods=nfoods)

    for o1, pos1 in foods_and_start_end.items():
        x1, y1 = pos1

        for o2, pos2 in foods_and_start_end.items():
            x2, y2 = pos2

            if o1 == o2:
                graph.set_distancePath(o1, o2, distance_path=DistancePath(distance=0, path=''))
            # calculate distance with BFS
            else:
                distance_path = run_bfs(board, x1, y1, x2, y2, garbage_board)

                if distance_path:
                    graph.set_distancePath(o1, o2, distance_path=distance_path)

    del foods_and_start_end['B']
    del foods_and_start_end['E']

    best_distance = float('inf')
    best_path = None

    for desiredK in range(k, nfoods + 1):
        for permutation in permutations(foods_and_start_end, desiredK):
            cur_distance = 0
            cur_path = ''

            nodes = ['B'] + list(permutation) + ['E']

            for i in range(len(nodes) - 1):
                edge = graph.get_distancePath(nodes[i], nodes[i + 1])
                if not edge:
                    cur_distance = float('inf')
                    break
                cur_distance += edge.distance
                cur_path += edge.path

            if cur_distance < best_distance:
                best_distance = cur_distance
                best_path = cur_path

    print(best_path)


if __name__ == '__main__':
    main()
