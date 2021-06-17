def printGraph(startNode, visited):
 
#     # Visit only those nodes who have any
#     # neighboring nodes to be traversed
#     if startNode.neighbors is not None:
 
#         # Loop through the neighboring nodes
#         # of this node. If source node not already
#         # visited, print edge from source to
#         # neighboring nodes. After visiting all
#         # neighbors of source node, mark its visited
#         # flag to true
#         for i in startNode.neighbors:
#             if visited[startNode.val] == False :
#                 print("edge %s-%s:%s-%s"%(hex(id(startNode)), hex(id(i)), startNode.val, i.val))
#                 if visited[i.val] == False:
#                     printGraph(i, visited)
#                     visited[i.val] = True