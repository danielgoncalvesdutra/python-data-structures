from collections import deque

#usa deque para criar uma fila
fila= deque(['abacate', 'bola', 'cachorro'])

#adicionanado um novo elemento
fila.append("dado")
print(fila) # deque(['abacate', 'bola', 'cachorro', 'dado'])

#remove o primeiro elemento adicionado à fila
fila.popleft()
print(fila) #deque(['bola', cachorro', 'dado'])