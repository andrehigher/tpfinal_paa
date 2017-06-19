# isomorphism example
test_case = 3
if test_case == 1:
    g = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'F'],
        'D': ['B', 'C'],
        'E': ['F'],
        'F': ['C', 'E']
    }

    h = {
        '1': ['2', '3'],
        '2': ['1', '3'],
        '3': ['1', '2']
    }
elif test_case == 2:
    g = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'F'],
        'D': ['B', 'C', 'E', 'F'],
        'E': ['D', 'F'],
        'F': ['C', 'D', 'E']
    }

    h = {
        '1': ['2', '5'],
        '2': ['1', '3'],
        '3': ['2', '4'],
        '4': ['3', '5'],
        '5': ['4', '1']
    }
elif test_case == 3:
    g = {
        'u': ['v', 'w'],
        'v': ['u', 'w'],
        'w': ['u', 'v', 'z'],
        'z': ['w']
    }

    h = {
        'a': ['b', 'f'],
        'b': ['a', 'c'],
        'c': ['b'],
        'd': ['e'],
        'e': ['d', 'f'],
        'f': ['a', 'e', 'g'],
        'g': ['f', 'h'],
        'h': ['g']
    }
else:
    g = {
        '1': ['2'],
        '2': ['1', '3'],
        '3': ['2']
    }

    h = {
        'A': ['B', 'C', 'D', 'E'],
        'B': ['A', 'C', 'D', 'E'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['A', 'B', 'C', 'E'],
        'E': ['A', 'B', 'C', 'D']
    }

degree_g = {}
degree_h = {}
candidates_g = {}
candidates_h = {}

# O(|V|)
for node in g:
    degree_g[node] = len(g[node])
    candidates_g[node] = []
for node in h:
    degree_h[node] = len(h[node])

# print 'List of degrees in G'
# for t in degree_g:
#     print t, degree_g[t]
# print 'List of degrees in H'
# for t in degree_h:
#     print t, degree_h[t]

# Check candidates of G and H with the vertex degree similarity
# O(|V|^2)
for node in h:
    for nodeg in g:
        if degree_h[node] >= degree_g[nodeg]:
            candidates_g[nodeg].append(node)

# Refine M
# O(|V|^2 x |E|^2)
for nodeg in g:
    for candidate in candidates_g[nodeg]:
        for neighboor in g[nodeg]:
            aux = False
            if len(candidates_g[neighboor]) > 0:
                for neighboor_candidate in candidates_g[neighboor]:
                    if neighboor_candidate in h[candidate]:
                        aux = True
                if aux == False:
                    candidates_g[nodeg].remove(candidate)

for nodeg in g:
    print nodeg, candidates_g[nodeg]


def ullmann(G, H, candidates, assignments):
    print G
    print H
    print candidates
    print assignments

assignments = 0
ullmann(g, h, candidates_g, assignments)