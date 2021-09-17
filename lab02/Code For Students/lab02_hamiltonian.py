from itertools import permutations



def graph_has_Hamiltonian_circuit(g):
    # g is a conected nondirected graph
    # decides whether g has a Hamiltonian circuit
    
    asignaciones = permutations(list(range(len(g))))
    
    #TODO


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

