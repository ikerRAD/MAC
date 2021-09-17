
def graph_has_Eulerian_circuit(g):
    # Inicializamos un vector booleano
   path= [ False for i in range(len(g)) ]
   #buscamos el circuito
   suma=0
   for i in range(len(g)):
       for j in range(len(g)):
           suma=suma+g[i][j]
       if(suma%2==1):
           path[i]=True
       suma=0    
           
   for i in path:
       if(not i):
           return i
   return True
  

def test():
    g1 = [[1, 1, 1, 0, 0],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1],
          [0, 1, 1, 1, 1]]
    assert not graph_has_Eulerian_circuit(g1)


    g2 = [[1, 1, 1, 0, 0, 0],
          [1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1],
          [0, 0, 0, 1, 1, 1]]
    
    assert graph_has_Eulerian_circuit(g2)

    g3 = [[1, 1, 1, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1, 1, 1, 1],
          [0, 1, 0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 1, 1, 0, 1, 1, 1],
          [0, 1, 1, 0, 1, 1, 1, 1],
          [0, 1, 1, 0, 0, 1, 1, 1]]
    
    assert not graph_has_Eulerian_circuit(g3)
    
    g4 = [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
          [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
          [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 1, 1],
          [0, 0, 0, 0, 0, 0, 1, 0, 1, 1]]
    
    assert graph_has_Eulerian_circuit(g4)
    
    g5 = [[1, 1, 0, 0],
          [1, 1, 1, 0],
          [0, 1, 1, 1],
          [0, 0, 1, 1]]
    
    assert not graph_has_Eulerian_circuit(g5)
    
 
  
    g6 = [[1, 1, 1, 0, 0, 0],
          [1, 1, 0, 1, 1, 0],
          [1, 0, 1, 1, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 1, 1, 0, 1, 0],
          [0, 0, 1, 1, 0, 1]]
    
    assert not graph_has_Eulerian_circuit(g6)
    
    g7 = [[1, 1, 0, 0],
          [1, 1, 1, 0],
          [0, 1, 1, 1],
          [0, 0, 1, 1]]
    
    assert not graph_has_Eulerian_circuit(g7)
    
    g8 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]
     
    
    assert not graph_has_Eulerian_circuit(g8)    

test()

