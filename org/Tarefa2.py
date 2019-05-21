condition = 10
pilha = [0, 255, 0, 255]
pilha.pop()
pilha.pop()
pilha.pop()
pilha.pop()
stckPt = 0
opertion = 0;
numb = 0;
aux0 = 0
aux1 = 0

while condition != 0:
	if len(pilha) > 0:
		aux0 = pilha.pop()
		print("Value of stack top:", aux0)
		print("Position of stack top:", len(pilha))
		pilha.append(aux0)
	else:
		print("Pilha vazia.")

	print("(1) Push.\n(2) Sum +.\n(3) Sub -.\n(4) Mult *.\n(5) Div /.\n(6) Exibir elementos da pilha\n(0) To exit.")
	condition = int(input())
	if condition == 1:
		aux0 = int(input())
		if aux0 < 256 and aux0 > -1:
			pilha.append(aux0)
			numb += 1
		else:
			print("Intervalo de números é entre(inclusive) 0 a 255(inclusive)")
	elif condition == 2:
		if numb < 2:
			print("Quantidade de operandos excede para a quantidade de números na pilha")
		elif numb > opertion:
			aux0 = pilha.pop()
			aux1 = pilha.pop()
			aux0 += aux1
			pilha.append(aux0)
			numb-=1
		else:
			print("Quantidade de operandos excede para a quantidade de números na pilha")
	elif condition == 3:
		if numb < 2:
			print("Quantidade de operandos excede para a quantidade de números na pilha")
		elif numb > opertion:
			aux0 = pilha.pop()
			aux1 = pilha.pop()
			aux0 = aux0 - aux1
			pilha.append(aux0)
			numb-=1
		else:
			print("Quantidade de operandos excede para a quantidade de números na pilha")
	elif condition == 4:
		if numb < 2:
			print("Quantidade de operandos excede para a quantidade de números na pilha")
		elif numb > opertion:
			aux0 = pilha.pop()
			aux1 = pilha.pop()
			aux0 *= aux1
			pilha.append(aux0)
			numb-=1
		else:
			print("Quantidade de operandos excede para a quantidade de números na pilha")
	elif condition == 5:
		if numb < 2:
			print("Quantidade de operandos excede para a quantidade de números na pilha")
		elif numb > opertion:
			aux0 = pilha.pop()
			aux1 = pilha.pop()
			aux0 = aux0//aux1
			pilha.append(aux0)
			numb-=1
		else:
			print("Quantidade de operandos excede para a quantidade de números na pilha")
	elif condition == 6:
		if len(pilha) > 0:
			print(pilha)
		else:
			print("Não há o que imprimir, pilha vazia")
	aux0 = pilha.pop()
	while aux0 > 255 or aux0 < 0:
		if aux0 > 255:
			aux0 -= 255
		else:
			aux0 += 255
	pilha.append(aux0)