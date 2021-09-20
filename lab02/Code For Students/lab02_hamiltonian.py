from itertools import permutations



def graph_has_Hamiltonian_circuit(g):
    # g is a conected nondirected graph
    # decides whether g has a Hamiltonian circuit
    
    asignaciones = permutations(list(range(len(g))))
    for i in list(asignaciones):
        if(isHamiltonian(g,i)):
            return True
    return False
    
def isHamiltonian(g,p):
    #checks if the given permutation defines a hamiltonian circuit
    for i in range(len(p)-1):
        if(g[p[i]][p[i+1]]==0):
            return False
    if(g[p[len(p)-1]][p[0]]==0):
        return False
    else:
        return True

#El coste del algoritmo es:
#El coste del checkeo isHamiltonian es O(n) ya que solo recorre las permutaciones
#En el algoritmo general, para cada permutación se checkea con el proceso anterior; es decir,
#en el caso peor, la llamada se hará n! veces. En conclusión, el coste del algoritmo es O(n*n!) (Muy costoso)

def test():
    g1 = [[1, 1, 1, 0, 0],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1],
          [0, 1, 1, 1, 1]]
    assert graph_has_Hamiltonian_circuit(g1)


    g2 = [[1, 1, 1, 0, 0, 0],
          [1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1],
          [0, 0, 0, 1, 1, 1]]
    
    assert graph_has_Hamiltonian_circuit(g2)

    g3 = [[1, 1, 1, 0, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 1, 1, 1],
          [1, 1, 1, 0, 1, 1, 1, 1],
          [0, 1, 0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 1, 0, 1, 0],
          [0, 1, 1, 1, 0, 1, 1, 1],
          [0, 1, 1, 0, 1, 1, 1, 1],
          [0, 1, 1, 0, 0, 1, 1, 1]]
    
    assert graph_has_Hamiltonian_circuit(g3)
    
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
    
    assert not graph_has_Hamiltonian_circuit(g4)
    
    g5 = [[1, 1, 1, 0, 0, 0],
          [1, 1, 0, 1, 1, 0],
          [1, 0, 1, 1, 1, 1],
          [0, 1, 1, 1, 0, 1],
          [0, 1, 1, 0, 1, 0],
          [0, 0, 1, 1, 0, 1]]
    
    assert not graph_has_Hamiltonian_circuit(g5)
    
    g6 = [[1, 1, 0, 0],
          [1, 1, 1, 0],
          [0, 1, 1, 1],
          [0, 0, 1, 1]]
    
    assert not graph_has_Hamiltonian_circuit(g6)
    
    g7 = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]
     
    
    assert not graph_has_Hamiltonian_circuit(g7)    

test()

