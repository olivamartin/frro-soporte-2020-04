numero = 1

def es_primo(numero):
 contador = 0
 for i in range(numero+1):
     if i != 0:
      if numero % i == 0:
          contador += 1
 if contador == 2:
     return True
 else:
     return False

print(es_primo(numero))
