import itertools
import random

class elements():

  def __init__(self):
    self.listaC =[]
    self.listaP =[]

  def combinacion(self):
    #print( list(itertools.combinations(range(0,10), 4)))
    self.listaC =  list(itertools.combinations_with_replacement(range(0,10), 4))

  def tomar(self):
    pos = random.randrange(len(self.listaC))
    return self.listaC[pos]

  def tomar1(self):
    pos = random.randrange(len(self.listaP))
    return self.listaP[pos]

  def cartesiano(self, repete):
    self.listaP = list(itertools.product(range(0,10),repeat = repete))
    


if __name__ ==  '__main__':
  gana = elements()
  #gana.combinacion()
  #print (gana.tomar1())
  result  = gana.cartesiano(4)
  #print(gana.listaP)
  print (gana.tomar1())
  result1  = gana.cartesiano(2)
  print (gana.tomar1())