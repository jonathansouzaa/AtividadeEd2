### Questão 2
import math

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class ListaEncadeada:
    def __init__(self,head=None):
        self.head = None

    def add(self, val):
      novoNo = Node(val)

      # If empty linked list is given
      if self.head is None:
          self.head = novoNo
          return

      # Traversing the given LL to reach the end
      aux = self.head
      while aux.next:
          aux = aux.next
      aux.next = novoNo

    def printLista(self):
      if self.head is None:
          return ""

      node = self.head
      while node:
          print(node.value, end = "   ")
          node = node.next

    def ordernarLista(self):
      lst = [] #this line was missing in an earlier solution
      while self.head:
          lst.append(self.head.value)
          self.head = self.head.next
      
      lst.sort()
      aux = ListaEncadeada()
      for num in lst:
        aux.add(num)
      return aux

if __name__ == '__main__':
    # Start with the empty list
    lista = ListaEncadeada()
    lista.add(1)
    lista.add(5)
    lista.add(4)
    lista.add(3)
    lista.add(2)
    lista.add(6)
    lista.add(7)
    print(f'A lista atualmente é:')
    lista.printLista()
    print('\n')
    listaOrdenada = lista.ordernarLista()
    print(f'A lista ordenada é: ')
    listaOrdenada.printLista()
    print('\n')

### Questão 3

#Como a estrutura de dados Pilha faz uso da lógica LIFO (o último a entrar é o primeiro a sair), para inverter uma String deve-se inserir letra por letra na pilha até a palavra estar toda empilhada, e depois, tirar letra por letra em uma string.*

!pip install pythonds
from pythonds.basic.stack import Stack

def reverterString(palavra):

    pilha = Stack()     

    for letra in palavra:       
        pilha.push(letra)  

    palavraInvertida = ''            
    while not pilha.isEmpty():
        palavraInvertida = palavraInvertida + pilha.pop()

    return palavraInvertida
print(reverterString("Leo Rocha"))



### Questão 5
from collections import deque

def navegarWeb():
  pilha = deque()
  menu = deque()
  menu.append("vazio")
  print(f"Site: {pilha}")
  encerrar = False
  count = 0
  while encerrar != True:
    escolha = int(input("Escolha a navegacão: 1 - Avancar | 2 - Voltar | 3 - Pagina Inicial | 4 - Encerrrar Aplicacao" ))
    if escolha == 1:
      count = count + 1 
      pilha.append(f'pagina{count} >' )
      menu.append(f'pagina{count} >')
      print(menu)
    elif escolha == 2:
      count= count - 1
      pilha.pop()
      menu.append(f'voltar >')
      if count == 0:
        menu.append(f'vazio')
      else:
        menu.append(f'pagina{count} >')
      print(menu)
    elif escolha == 3:
      count = 1
      pilha.clear()
      pilha.append(f'pagina{count} >')
      menu.append(f' voltar pagina inicial')
      menu.append(f'pagina{count}')
      print(menu)
    elif escolha == 4:
      menu.append(f'fechar aplicacao')
      pilha.clear()
      encerrar = True
      print(menu)
  print('finalizado')

navegarWeb()

### Questão 6
class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class ListaEncadeada:
    def __init__(self,head=None):
        self.head = None

    def add(self, val):
      novoNo = Node(val)

      # If empty linked list is given
      if self.head is None:
          self.head = novoNo
          return

      # Traversing the given LL to reach the end
      aux = self.head
      while aux.next:
          aux = aux.next
      aux.next = novoNo

    def printLista(self):
      if self.head is None:
          return ""

      node = self.head
      while node:
          print(node.value, end = "   ")
          node = node.next

    def acharMeio(self):
      meio = self.head
      fim = self.head
      while(fim.next and fim.next.next):
          fim = fim.next.next
          meio = meio.next
      
      return meio

if __name__ == '__main__':
    # Start with the empty list
    lista = ListaEncadeada()
    lista.add(1)
    lista.add(2)
    lista.add(3)
    lista.add(4)
    lista.add(5)
    print(f'A lista atualmente é:')
    lista.printLista()
    print('\n')

    meio = lista.acharMeio()
    print("Nó do Meio: ")
    print(meio.value)

### Questão 7

#Resposta: Uma fila do tipo FIFO (First In, First Out)

from queue import Queue

fila = Queue()
def tocar (lista):
  while not lista.empty():
    print(f'\n  Agora esta tocando: {lista.get()}')
  print('Fim da Lista de Músicas')

rodar = True
fila.put(input("Adicione uma Música:  "))
print("Adicionada com Sucesso")
while (rodar):
  decisao = int(input("1 - Adicionar mais uma musica \n 2 - Tocar Playlist \n"))
  if decisao == 1:
    fila.put(input('Digite a música'))
    print("Adicionada com Sucesso")
  if decisao == 2:
    rodar = False
    tocar(fila)


### Questão 8
#Apesar de não ser o algoritmo mais rápido, o bubble sort funciona muito bem para quantidade média de itens a serem ordenados 
from heapq import heappop, heappush
def ordenacaoHeap(array):
    heap = []
    for element in array:
        heappush(heap, element)

    ordered = []

    while heap:
        ordered.append(heappop(heap))

    return ordered

array = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2]
print(ordenacaoHeap(array))
