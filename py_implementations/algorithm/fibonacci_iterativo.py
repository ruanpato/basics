'''Simple implementation of fibonacci iterative, who receive a integer and show n numbers of the sequence'''
lista=[0,1]

j=int(input())

while(len(lista) < j):
    lista.append(lista[len(lista)-1]+lista[len(lista)-2])

for i in range(0, j):
    print(lista[i], end=' ')
