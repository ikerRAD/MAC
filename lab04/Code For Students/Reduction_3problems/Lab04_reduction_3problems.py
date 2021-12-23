from vertex_cover import solve_vc

#Hacemos algo parecido a un switch case (en python no hay)
def multisolve(graph, problem): 
    if problem=="VERTEX COVER":#nos viene solucionado
        return solve_vc(graph)
    elif problem=="CLIQUE":
        return solve_cl(graph)
    elif problem=="INDEPENDENT SET":
        return solve_is(graph)        
    else:#error
        return -1
#Invertimos la solución de vertex cove, todos los nodos que no estén en el vertex cover
#serán independent set, transformación que tarda O(n)
def solve_is(graph):
    aux=solve_vc(graph)
    sol=[0 for i in range(len(graph)) ]
    for i in range(len(graph)):
        if not aux[i]:
            sol[i]=1
    return sol
#Invertimos el grafo haciendo que los 0's sean 1's en la matriz de adyacencia y viceversa
#el único problema es que cuando i=j, debería seguir siendo uno pero se vuleve 0, aunque
#como no alteraría el funcionamiento del algoritmo, no lo cambiamos, esta transformación
#tarda O(n^2). Una vez hecho, sabemos que el independent set del inverso, será el clique
#de nuestro grafo
def solve_cl(graph):
    g2 = [[abs(graph[i][j]-1) for i in range(len(graph)) ] for j in range(len(graph)) ]
    return solve_is(g2)
    
def test():
   graph = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]]
   
   sol_vertex = multisolve(graph, "VERTEX COVER")
   sol_clique = multisolve(graph, "CLIQUE")
   sol_independent_set =  multisolve(graph, "INDEPENDENT SET")
   
   assert sol_vertex in [[0,0,1,1], [1,0,0,1], [0,1,1,0]]
   assert sol_independent_set in [[1,0,0,1],[1,1,0,0],[0,1,1,0]]
   assert sol_clique in [[1,0,1,0],[0,0,1,1],[0,1,0,1]]
   
   graph = [[0,1,1],[1,0,1],[1,1,0]]
   
   sol_vertex = multisolve(graph, "VERTEX COVER")
   sol_clique = multisolve(graph, "CLIQUE")
   sol_independent_set =  multisolve(graph, "INDEPENDENT SET")
     
   assert sol_vertex in [[0,1,1], [1,0,1], [1,1,0]]
   assert sol_independent_set in [[1,0,0],[0,1,0],[0,0,1]]
   assert sol_clique in [[1,1,1]]


test()
