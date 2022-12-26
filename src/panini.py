import random

def generar_sobre(n,lista_cartas):
  # abre un sobre de n cartas
  #@param n: numero de cartas q contiene el sobre
  #@type n: int
  #@param lista_cartas: lista con las cartas de IE Champs
  #@type lista_cartas: [Carta()] 
  #@return: lista de cartas obtenidas
  #@rtype: [Carta()]
  res= []
  for i in range(n):
    x = random.randint(0,len(lista_cartas)-1)
    res.append(lista_cartas[x])
  return res
