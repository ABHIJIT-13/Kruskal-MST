def root(vertex):
	if rootIds[vertex] == vertex:
		return vertex
	else:
		while rootIds[vertex] != vertex:
			rootIds[vertex] = rootIds[rootIds[vertex]]
			vertex = rootIds[vertex]
		return vertex			


def union(u,v):
	uroot = root(u)
	vroot = root(v)
	rootIds[v] = rootIds[u]
	return





def Kruskal(GE):
	global rootIds
	miniWeight = 0

	for edge in GE:
		u = edge[0]
		v = edge[1]
		weight= edge[2]

		if root(u) != root(v):
			miniWeight += weight
			union(u,v)
	return miniWeight		









V,E = map(int,input().split())
GE = []
for i in range(E):
	GE.append(list(map(int,input().split())))
GE = sorted(GE, key=lambda x:x[2])
rootIds = list(range(V+1))

print(Kruskal(GE))	