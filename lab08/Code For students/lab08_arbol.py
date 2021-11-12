from random import randint
  
def prim_algorithm(graph):
    # Lista de nodos marcados
    marcado = [False]*len(graph)
    nodo = randint(0,len(marcado)-1)
    marcado[nodo] = True

    #futuro arbol
    output = [[float("inf") for i in range(len(graph))] for j in range(len(graph))]
    #mientras queden nodos por marcar
    while False in marcado:
        minimo = float("inf")
        nodomin = -1
        incimin = -1
        #para todo nodo marcado
        for nodo in range(len(graph)):
            if marcado[nodo]:
                for incidente in range(len(graph)):
                    #si el nodo es incidente y no marcado, comprobamos
                    if graph[nodo][incidente] != float("inf") and not marcado[incidente]:
                        #vemos si tiene arista con peso mínimo
                        if graph[nodo][incidente] < minimo:
                            nodomin = nodo
                            incimin = incidente
                            minimo = graph[nodo][incidente]
                            
        output[nodomin][incimin]=minimo
        output[incimin][nodomin]=minimo
        marcado[incimin] = True

    
    return output
    
 

def test():
    
    g1 =  [[float("inf"), 2.0],
           [2.0, float("inf")]]
    
    assert prim_algorithm(g1) == g1
    
    
       
    g2 = [[float("inf"), 5.0, 3.0],
          [5.0, float("inf"), float("inf")],
          [3.0, float("inf"), float("inf")]]
    
    assert prim_algorithm(g2) == g2
        
    
    
    g3 = [[float("inf"), 1.0, 2.0, 3.0, 4.0],
          [1.0, float("inf"), float("inf"), float("inf"), 8.0],
          [2.0, float("inf"), float("inf"), 2.0, 3.0],
          [3.0, float("inf"), 2.0, float("inf"), 5.0],
          [4.0, 8.0, 3.0, 5.0, float("inf")]]
    
    assert prim_algorithm(g3) == [[float("inf"), 1.0, 2.0, float("inf"), float("inf")], 
                                  [1.0, float("inf"), float("inf"), float("inf"), float("inf")], 
                                  [2.0, float("inf"), float("inf"), 2.0, 3.0], 
                                  [float("inf"), float("inf"), 2.0, float("inf"), float("inf")], 
                                  [float("inf"), float("inf"), 3.0, float("inf"), float("inf")]] 
    
    
        
    g4 = [[float("inf"), 6.0, 2.0, 5.0],
          [6.0, float("inf"), 4.0, float("inf")],
          [2.0, 4.0, float("inf"), 2.0],
          [5.0, float("inf"), 2.0, float("inf")]]
    
    assert prim_algorithm(g4) == [[float("inf"), float("inf"), 2.0, float("inf")], 
                                  [float("inf"), float("inf"), 4.0, float("inf")], 
                                  [2.0, 4.0, float("inf"), 2.0], 
                                  [float("inf"), float("inf"), 2.0, float("inf")]]
    
    
       
    g5 = [[float("inf"), 10.0, 1.0, float("inf"), float("inf"), float("inf")],
          [10.0, float("inf"), float("inf"), 5.0, 4.0, float("inf")],
          [1.0, float("inf"), float("inf"), 8.0, 2.0, 3.0],
          [float("inf"), 5.0, 8.0, float("inf"), float("inf"), 2.0],
          [float("inf"), 4.0, 2.0, float("inf"), float("inf"), float("inf")],
          [float("inf"), float("inf"), 3.0, 2.0, float("inf"), float("inf")]]
    
    assert prim_algorithm(g5) == [[float("inf"), float("inf"), 1.0, float("inf"), float("inf"), float("inf")], 
                                  [float("inf"), float("inf"),float("inf"), float("inf"), 4.0, float("inf")], 
                                  [1.0, float("inf"), float("inf"), float("inf"), 2.0, 3.0], 
                                  [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 2.0], 
                                  [float("inf"), 4.0, 2.0, float("inf"), float("inf"), float("inf")], 
                                  [float("inf"), float("inf"), 3.0, 2.0, float("inf"), float("inf")]]
    
    
    
    g6 = [[float("inf"), 3.0, 1.0, float("inf"), float("inf"), float("inf"), float("inf")],
          [3.0, float("inf"), 8.0, 10.0, 5.0, float("inf"), float("inf")],
          [1.0, 8.0, float("inf"), float("inf"), float("inf"), float("inf"), float("inf")],
          [float("inf"), 10.0, float("inf"), float("inf"), 6.0, float("inf"), 9.0],
          [float("inf"), 5.0, float("inf"), 6.0, float("inf"), 1.0, 2.0],
          [float("inf"), float("inf"), float("inf"), float("inf"), 1.0, float("inf"), 4.0],
          [float("inf"),float("inf"),float("inf"), 9.0, 2.0, 4.0, float("inf")]]
    
    
    assert prim_algorithm(g6) == [[float("inf"), 3.0, 1.0, float("inf"), float("inf"), float("inf"), float("inf")], 
                                 [3.0, float("inf"), float("inf"), float("inf"), 5.0, float("inf"), float("inf")], 
                                 [1.0, float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf")], 
                                 [float("inf"), float("inf"), float("inf"), float("inf"), 6.0, float("inf"), float("inf")], 
                                 [float("inf"), 5.0, float("inf"), 6.0, float("inf"), 1.0, 2.0], 
                                 [float("inf"), float("inf"), float("inf"), float("inf"), 1.0, float("inf"), float("inf")], 
                                 [float("inf"), float("inf"), float("inf"), float("inf"), 2.0, float("inf"), float("inf")]]

    

test()
