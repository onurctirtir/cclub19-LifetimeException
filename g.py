# Python program for implementation of Ford Fulkerson algorithm

from collections import defaultdict

#This class represents a directed graph using adjacency matrix representation
class Graph:

	def __init__(self,graph):
		self.graph = graph # residual graph
		self. ROW = len(graph)
		#self.COL = len(gr[0])


	'''Returns true if there is a path from source 's' to sink 't' in
	residual graph. Also fills parent[] to store the path '''
	def BFS(self,s, t, parent):

		# Mark all the vertices as not visited
		visited =[False]*(self.ROW)

		# Create a queue for BFS
		queue=[]

		# Mark the source node as visited and enqueue it
		queue.append(s)
		visited[s] = True

		# Standard BFS Loop
		while queue:

			#Dequeue a vertex from queue and print it
			u = queue.pop(0)

			# Get all adjacent vertices of the dequeued vertex u
			# If a adjacent has not been visited, then mark it
			# visited and enqueue it
			for ind, val in enumerate(self.graph[u]):
				if visited[ind] == False and val > 0 :
					queue.append(ind)
					visited[ind] = True
					parent[ind] = u

		# If we reached sink in BFS starting from source, then return
		# true, else false
		return True if visited[t] else False


	# Returns tne maximum flow from s to t in the given graph
	def FordFulkerson(self, source, sink):

		# This array is filled by BFS and to store path
		parent = [-1]*(self.ROW)

		max_flow = 0 # There is no flow initially

		# Augment the flow while there is path from source to sink
		while self.BFS(source, sink, parent) :

			# Find minimum residual capacity of the edges along the
			# path filled by BFS. Or we can say find the maximum flow
			# through the path found.
			path_flow = float("Inf")
			s = sink
			while(s != source):
				path_flow = min (path_flow, self.graph[parent[s]][s])
				s = parent[s]

			# Add path flow to overall flow
			max_flow += path_flow

			# update residual capacities of the edges and reverse edges
			# along the path
			v = sink
			while(v != source):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v = parent[v]

		return max_flow


# Create a graph given in the above diagram

T,B = map(int, input().split())

tower = {}

graph = [0] * (T + T - 2)

for i in range((T + T - 2)):
    graph[i] = [0] * (T + T - 2)

for i in range(T - 2):
    x , cost = map(int, input().split())
    graph[2 * x - 3][2 * x - 2] = cost
    graph[2 * x - 2][2 * x - 3] = cost


#for i in range(len(graph)):
#    print(graph[i])

for i in range(B):
    x, y, z = map(int, input().split())

    if (x - 1 == 0 and y - 1 + T - 2 == 2 * T - 3):
        graph[x - 1][y - 1 + T - 2] = z
        graph[y - 1 + T - 2][x - 1] = z


    elif x - 1 == 0 or x - 1 + T - 2 == 2 * T - 3:
        if x - 1 + T - 2 == 2 * T - 3:
            x = 2 * T - 2
        graph[x - 1][2 * y - 3] = z
        graph[2 * y - 2][x - 1] = z

    elif y - 1 == 0 or y - 1 + T - 2 == 2 * T - 3:
        if y - 1 + T - 2 == 2 * T - 3:
            y = 2 * T - 2
        graph[2 * x - 2][y - 1] = z
        graph[y - 1][2 * x - 3] = z

    else:
        graph[2 * x - 2][2 * y - 3] = z
        graph[2 * y - 2][2 * x - 3] = z


bum1, bum2 = map(int, input().split())

#for i in range(len(graph)):
#    print(graph[i])


g = Graph(graph)

source = 0; sink = 2 * T - 3

print(g.FordFulkerson(source, sink))
