# Crie uma lista com 60 números começando com o valor 1 e indo até o número 60 (ou seja, o número 60 deve estar na lista).
minha_lista = list(range(1, 61))
#for n in range(1, 61):
print(minha_lista, end=" ")
print()

# Imprima todos os itens da sua lista de índice par. Imprima o índice e o item.
print('índice | item')
print('------ | ----')
for i, item in enumerate(minha_lista):
  if i % 2 == 0:
     print(f'   {i}   |  {item}')
print()
#print()