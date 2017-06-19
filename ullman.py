import networkx as nx
from networkx.algorithms import isomorphism

def search(graph, subgraph, assignments, possible_assignments):
	i=len(assignments)
  # Make sure that every edge between assigned vertices in the subgraph is also an
  # edge in the graph.
	for edge in subgraph.edges():
		if edge[0]<i and edge[1]<i:
			if not graph.has_edge(assignments[edge[0]],assignments[edge[1]]):
				return False

  # If all the vertices in the subgraph are assigned, then we are done.
	if i==subgraph.number_of_nodes():
		return True

  # Otherwise, go through all the possible assignments for the next vertex of
  # the subgraph and try it.
	for j in possible_assignments:
		if j not in assignments:
			assignments.append(j)
			if search(graph,subgraph,assignments, possible_assignments):
        		# This worked, so we've found an isomorphism.
				return True
			assignments.pop()

def find_isomporhism(graph, subgraph):
	assignments = []
	possible_assignments = [[True]*graph.number_of_nodes() for i in range(subgraph.number_of_nodes())]
	print 'possible_assignments', possible_assignments
	if search(graph, subgraph, assignments, possible_assignments):
		return assignments
	return None

G=nx.Graph()
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(2,3)
G.add_edge(2,5)
G.add_edge(3,4)
G.add_edge(3,5)
G.add_edge(4,5)

# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
# G.add_node(4)
# G.add_node(5)
# G.add_node(6)
# G.add_edge(1,2)
# G.add_edge(1,3)
# G.add_edge(3,4)
# G.add_edge(2,4)
# G.add_edge(2,5)
# G.add_edge(2,6)

H=nx.Graph()
H.add_node(1)
H.add_node(2)
H.add_node(3)
H.add_edge(1,2)
H.add_edge(1,3)
H.add_edge(2,3)

# H.add_node(1)
# H.add_node(2)
# H.add_node(3)
# H.add_node(4)
# H.add_node(5)
# H.add_edge(1,2)
# H.add_edge(1,3)
# H.add_edge(3,4)
# H.add_edge(2,4)
# H.add_edge(2,5)

# print find_isomporhism(H, G)

GM = isomorphism.GraphMatcher(H,G)
print GM.subgraph_is_isomorphic()