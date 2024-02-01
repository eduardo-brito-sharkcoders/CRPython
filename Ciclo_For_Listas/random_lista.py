from random import choice

lista_paises = ["portugal", "espanha", "irlanda", "china", "inglaterra"]

pais_escolhido = choice(lista_paises)

primeira_letra = pais_escolhido[0]
ultima_letra = pais_escolhido[len(pais_escolhido) - 1]

print(pais_escolhido)
print(len(pais_escolhido))
print(primeira_letra)
print(ultima_letra)

