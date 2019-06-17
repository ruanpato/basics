tropas = []
comandantes = []
menor_c = 0 # menor capacidade
qtd_total = 0 # Quantidade total de tropas
class Tropa:
    def __init__(self, tipo, quantidade, nivel, nome):
        self.set_tipo(tipo)
        self.set_quantidade(quantidade)
        self.set_nivel(nivel)
        self.set_nome(nome)
    # Getters
    def get_tipo(self):
        return self.tipo
    def get_quantidade(self):
        return self.quantidade
    def get_nivel(self):
        return self.nivel
    def get_nome(self):
        return self.nome
    # Setters
    def set_quantidade(self, value):
        self.quantidade = value
    def set_tipo(self, value):
        self.tipo = value
    def set_nivel(self, value):
        self.nivel = value
    def set_total(self, value):
        self.total = value
    def set_nome(self, value):
        self.nome = value
    # Pega as tropas salvas no 
    def get_from_file(self):
        arquivo = open('tropas.in', 'r')
        total = 0
        linhas = arquivo.readlines() # Coloca cada linha (\n) em uma posição de linhas
        if(linhas == ''):
            print("Arquivo vazio.") # Adicionar a opção de adicionar ou editar a quantidade de tropas
            exit(0)
        else:
            tropas.pop()
            n = len(linhas)
            for i in range(n): # Pega as tropas da linha e coloca na lista de objetos chamda de tropas
                aux_t, aux_n, aux_q, aux_p = linhas[i].split('-')
                aux_p = aux_p.replace("\n", "")
                total += int(aux_q)
                tropas.append(Tropa(aux_t, int(aux_q), int(aux_p), aux_n))
        arquivo.close()
        return total
class Comandante:
    def __init__(self, nome, capacidade, nivel): # Método construtor de comandante
        self.nome = nome
        self.capacidade = capacidade
        self.nivel = nivel
        self.tropas = []
    # Getters(obs. python não precisa de getters)
    def get_nome(self):
        return self.nome
    def get_capacidade(self):
        return self.capacidade
    def get_nivel(self):
        return self.nivel

    # Setters
    def set_nome(self, value):
        self.nome = value
    def set_capacidade(self, value):
        self.capacidade = value
    def set_nivel(self, value):
        self.nivel = value

###################### MAIN ##################
tropas.append(Tropa('',0,0, ''))
qtd_total = tropas[0].get_from_file()
n = len(tropas)
for i in range(n):
    print(tropas[i].get_tipo(), "\n--->nivel:", tropas[i].get_nivel(), " - Quantidade:", tropas[i].get_quantidade(), sep='')
print(qtd_total)

qtd = int(input("Quantidade de comandantes: ")) # Recebe a quantidade de comandantes
# Recebe os valores de comandantes:
for i in range(qtd):
    aux_n = i#input("Digite o nome do comandante: ")
    aux_c = 100000#input("Digite a capacidade do comandante: ")
    aux_p = 100000#input("Digite o nivel do comandante: ")
    comandantes.append(Comandante(aux_n, aux_c, aux_p))

# Dividindo
for i in range(n):          # Quantidade de tropas
    for j in range(qtd):    # Quantidade de comandantes
        if(j == 0):
            comandantes[j].tropas.append(Tropa(tropas[i].get_tipo(), (tropas[i].get_quantidade()//qtd + tropas[i].get_quantidade()%qtd ), tropas[i].get_nivel(), tropas[i].get_nome() ))
        else:
            comandantes[j].tropas.append(Tropa(tropas[i].get_tipo(), (tropas[i].get_quantidade()//qtd), tropas[i].get_nivel(), tropas[i].get_nome() ))
for i in range(100):
    print('\n')
print(" |Infantaria       |Cavalaria              |Arquearia              |Cerco           ")
for i in range(2):
    tropas_ordenadas_por_nivel = sorted(comandantes[i].tropas, key = Tropa.get_nivel) # Lista auxiliar
    total_tropas = 0
    if(i == 0):
       print('\n|   Comandante ', comandantes[i].get_nome()+1, '                          |  ', sep='')
    else:
        print('\n| Outros Comandantes                    |  ', sep='')
    for j in range(n):
        if(j%4==0):
            print('\n', tropas_ordenadas_por_nivel[j].get_nivel(), '|', tropas_ordenadas_por_nivel[j].get_nome(), ' ', tropas_ordenadas_por_nivel[j].get_quantidade(), sep='', end='')
        else:
            print(' |', tropas_ordenadas_por_nivel[j].get_nome(), ' ', tropas_ordenadas_por_nivel[j].get_quantidade(), sep='', end='')
        total_tropas += tropas_ordenadas_por_nivel[j].get_quantidade()
    print("\n| Total =", total_tropas)
    tropas_ordenadas_por_nivel.clear()