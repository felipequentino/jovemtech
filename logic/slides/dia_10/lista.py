#lista.reverse()
#print(lista)

lista = [0, 1, 2, 3, 4, 5, 6] 
backup = lista.copy()
tamanho = len(lista)

for i in range(tamanho):
    # 1ª iteração -> i = 0 
    # 2ª ITERação -> i = 1 | (1+1) * -1 = -2
    indice_negativo = (i+1) * -1 # | 0 <-> -1
    lista[i] = backup[indice_negativo]
    lista[indice_negativo] = backup[i]

print(backup)
print(lista)    