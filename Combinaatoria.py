import itertools
import random

class elements():
    def __init__(self):
        self.listaP =[]
        self.mirange = range(0,10)

    def setRepete(self, number):
        self.repete = number

    def combinacion(self):
        self.listaP =  list(itertools.combinations_with_replacement(self.mirange, self.repete))

    def tomar(self):
        pos = random.randrange(len(self.listaP))
        return self.listaP[pos]

    def cartesiano(self):
        self.listaP = list(itertools.product(self.mirange, repeat = self.repete))
    


if __name__ ==  '__main__':
  gana4numero = elements()
  gana4numero.setRepete(4)
  gana4numero.combinacion()
  print (gana4numero.tomar())
  gana4numero.setRepete(2)
  gana4numero.cartesiano()
  print (gana4numero.tomar())
  