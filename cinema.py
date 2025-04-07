#Isaac Koga Carone

# Todos os F = filmes, todos os S = sessões, valores 1 e 2 após S e F indicam o tipo de filme e sessão

filmes_assentos = {"F1_S1": 50, "F1_S2": 50,
                   "F2_S1": 40, "F2_S2": 40,
                   "F3_S1": 30, "F3_S2": 30}
qtd_ingressos = {
    "F1_S1": {"Inteira": 0, "Meia": 0, "VIP": 0}, 
    "F1_S2": {"Inteira": 0, "Meia": 0, "VIP": 0},
    "F2_S1": {"Inteira": 0, "Meia": 0, "VIP": 0},
    "F2_S2": {"Inteira": 0, "Meia": 0, "VIP": 0},
    "F3_S1": {"Inteira": 0, "Meia": 0, "VIP": 0},
    "F3_S2": {"Inteira": 0, "Meia": 0, "VIP": 0}}

valores_arrecadados = {
    "F1_S1": {"Inteira": 0.0, "Meia": 0.0, "VIP": 0.0},
    "F1_S2": {"Inteira": 0.0, "Meia": 0.0, "VIP": 0.0},
    "F2_S1": {"Inteira": 0.0, "Meia": 0.0, "VIP": 0.0},
    "F2_S2": {"Inteira": 0.0, "Meia": 0.0, "VIP": 0.0},
    "F3_S1": {"Inteira": 0.0, "Meia": 0.0, "VIP": 0.0},
    "F3_S2": {"Inteira": 0.0, "Meia": 0.0, "VIP": 0.0}}

poltronas = {
    "F1_S1": ["D"] * 50,
    "F1_S2": ["D"] * 50,
    "F2_S1": ["D"] * 40,
    "F2_S2": ["D"] * 40,
    "F3_S1": ["D"] * 30,
    "F3_S2": ["D"] * 30}

precos = [20, 10, 30, 15, 7.50, 22.50, 5]

total_qtd_ingressos = []
receita_total_dia = []

avaliacoes = {
    "F1": {"quantidade": 0, "notas": 0},
    "F2": {"quantidade": 0, "notas": 0},
    "F3": {"quantidade": 0, "notas": 0}}

def calculos(precos, indice, qtd, valor, filme_sessao, tipo_ingresso, quantidade):
    preco = precos[indice] * quantidade
    qtd[filme_sessao][tipo_ingresso] += quantidade
    valor[filme_sessao][tipo_ingresso] += preco
    total_qtd_ingressos.append(quantidade)
    receita_total_dia.append(preco)
    print("O valor a pagar é igual a R${:.2f}".format(preco))


def exibir_poltronas(sala):
    print("\nPoltronas disponíveis:")
    for i, poltrona in enumerate(poltronas[sala]):
        if poltrona == 'D':
            print(f"{i + 1:02d}", end=" ")
        else:
            print("XX", end=" ")
        if (i + 1) % 10 == 0:
            print()
    print()

def escolher_poltronas(sala, quantidade, poltronas):
    poltronas_escolhidas = []
    cont = 0

    while cont < quantidade:
        lugar = int(input("Escolha sua poltrona (1 a {}): ".format(len(poltronas[sala]))))
        if lugar < 1 or lugar > len(poltronas[sala]):
            print("Número de poltrona inválido. Escolha novamente.")
            continue

        if poltronas[sala][lugar - 1] == 'D':  # Poltrona disponível
            print("Poltrona disponível\n")
            poltronas[sala][lugar - 1] = 'I'  # Marca a poltrona como indisponível
            poltronas_escolhidas.append(lugar)
            cont += 1
        else:
            print("Poltrona indisponível. Escolha outra.\n")
    print("Poltronas escolhidas:", poltronas_escolhidas)
    return poltronas_escolhidas


def info(filmes_assentos, indice_f, precos, indice_i, indice_m, indice_v):
    print("\nAssentos disponíveis: {}".format(filmes_assentos[indice_f]))
    print("TIPOS DE INGRESSO:")
    print("\n 1. Inteira = R${} \n 2. Meia Entrada = R${} \n 3. VIP = R${} \n ".format(precos[indice_i], precos[indice_m], precos[indice_v]))

def avaliacao(feedback, nota, filme):
    feedback[filme]["quantidade"] += 1
    if (nota <= 5) and (nota >= 1):
        feedback[filme]["notas"] += nota
    else:
        print("Opção inválida")

def imprime_linha_p(v, j):
     for i in range(v):
        print('#', end="")
     print(f" {v} - Filme: {j}")
     
def grafico_barra(lista):
     j = 1
     for valor in lista:
          imprime_linha_p(valor, j)
          j += 1

menu = 0
while menu != 8:
    print("""
            --------------------- MENU ---------------------
            | 1. Comprar ingressos para Filme 1 - Sessão 1 |
            | 2. Comprar ingressos para Filme 1 - Sessão 2 |
            | 3. Comprar ingressos para Filme 2 - Sessão 1 |
            | 4. Comprar ingressos para Filme 2 - Sessão 2 |
            | 5. Comprar ingressos para Filme 3 - Sessão 1 |
            | 6. Comprar ingressos para Filme 3 - Sessão 2 |
            | 7. Avaliar um filme                          |
            | 8. Encerrar o dia e exibir o relatório       |
            ------------------------------------------------""")
    menu = int(input("\n        Digite o número correspondente a opção que deseja escolher: "))

    if menu == 1:
        sala = "F1_S1"
        exibir_poltronas(sala)
        info(filmes_assentos, "F1_S1", precos, 0, 1, 2)
        quantidade = int(input("Quantas poltronas deseja selecionar? "))
        poltronas_escolhidas = escolher_poltronas(sala, quantidade, poltronas)
        ingresso = int(input("Digite o número correspondente ao ingresso que você quer: "))
        
        if quantidade <= filmes_assentos["F1_S1"]:
            filmes_assentos["F1_S1"] -= quantidade
            if ingresso == 1:
                calculos(precos, 0, qtd_ingressos, valores_arrecadados, "F1_S1", "Inteira", quantidade)
            elif ingresso == 2:
                calculos(precos, 1, qtd_ingressos, valores_arrecadados, "F1_S1", "Meia", quantidade)
            elif ingresso == 3:
                calculos(precos, 2, qtd_ingressos, valores_arrecadados, "F1_S1", "VIP", quantidade)  
            else:
                print("Tipo de ingresso inválido.")
                filmes_assentos["F1_S1"] += quantidade
        else:
            print("Quantidade de ingressos indisponível.")

    elif menu == 2:
        sala = "F1_S2"
        exibir_poltronas(sala)
        info(filmes_assentos, "F1_S2", precos, 0, 1, 2)
        quantidade = int(input("Quantas poltronas deseja selecionar? "))
        poltronas_escolhidas = escolher_poltronas(sala, quantidade, poltronas)
        ingresso = int(input("Digite o número correspondente ao ingresso que você quer: "))

        if quantidade <= filmes_assentos["F1_S2"]:
            filmes_assentos["F1_S2"] -= quantidade
            if ingresso == 1:
                calculos(precos, 0, qtd_ingressos, valores_arrecadados, "F1_S2", "Inteira", quantidade)
            elif ingresso == 2:
                calculos(precos, 1, qtd_ingressos, valores_arrecadados, "F1_S2", "Meia", quantidade)
            elif ingresso == 3:
                calculos(precos, 2, qtd_ingressos, valores_arrecadados, "F1_S2", "VIP", quantidade)
            else:
                print("Tipo de ingresso inválido.")
                filmes_assentos["F1_S2"] += quantidade
        else:
            print("Quantidade de ingressos indisponível.")

    elif menu == 3:
        sala = "F2_S1"
        exibir_poltronas(sala)
        info(filmes_assentos, "F2_S1", precos, 3, 4, 5)
        quantidade = int(input("Quantas poltronas deseja selecionar? "))
        poltronas_escolhidas = escolher_poltronas(sala, quantidade, poltronas)
        ingresso = int(input("Digite o número correspondente ao ingresso que você quer: "))

        if quantidade <= filmes_assentos["F2_S1"]:
            filmes_assentos["F2_S1"] -= quantidade
            if ingresso == 1:
                calculos(precos, 3, qtd_ingressos, valores_arrecadados, "F2_S1", "Inteira", quantidade)
            elif ingresso == 2:
                calculos(precos, 4, qtd_ingressos, valores_arrecadados, "F2_S1", "Meia", quantidade)
            elif ingresso == 3:
                calculos(precos, 5, qtd_ingressos, valores_arrecadados, "F2_S1", "VIP", quantidade)
            else:
                print("Tipo de ingresso inválido.")
                filmes_assentos["F2_S1"] += quantidade
        else:
            print("Quantidade de ingressos indisponível.")

    elif menu == 4:
        sala = "F2_S2"
        exibir_poltronas(sala)
        info(filmes_assentos, "F2_S2", precos, 3, 4, 5)
        quantidade = int(input("Quantas poltronas deseja selecionar? "))
        poltronas_escolhidas = escolher_poltronas(sala, quantidade, poltronas)
        ingresso = int(input("Digite o número correspondente ao ingresso que você quer: "))

        if quantidade <= filmes_assentos["F2_S2"]:
            filmes_assentos["F2_S2"] -= quantidade
            if ingresso == 1:
                calculos(precos, 3, qtd_ingressos, valores_arrecadados, "F2_S2", "Inteira", quantidade)
            elif ingresso == 2:
                calculos(precos, 4, qtd_ingressos, valores_arrecadados, "F2_S2", "Meia", quantidade)
            elif ingresso == 3:
                calculos(precos, 5, qtd_ingressos, valores_arrecadados, "F2_S2", "VIP", quantidade)
            else:
                print("Tipo de ingresso inválido.")
                filmes_assentos["F2_S2"] += quantidade
        else:
            print("Quantidade de ingressos indisponível.")

    elif menu == 5:
        sala = "F3_S1"
        exibir_poltronas(sala)
        info(filmes_assentos, "F3_S1", precos, 1, 6, 3)
        quantidade = int(input("Quantas poltronas deseja selecionar? "))
        poltronas_escolhidas = escolher_poltronas(sala, quantidade, poltronas)
        ingresso = int(input("Digite o número correspondente ao ingresso que você quer: "))

        if quantidade <= filmes_assentos["F3_S1"]:
            filmes_assentos["F3_S1"] -= quantidade
            if ingresso == 1:
                calculos(precos, 1, qtd_ingressos, valores_arrecadados, "F3_S1", "Inteira", quantidade)
            elif ingresso == 2:
                calculos(precos, 6, qtd_ingressos, valores_arrecadados, "F3_S1", "Meia", quantidade)
            elif ingresso == 3:
                calculos(precos, 3, qtd_ingressos, valores_arrecadados, "F3_S1", "VIP", quantidade)
            else:
                print("Tipo de ingresso inválido.")
                filmes_assentos["F3_S1"] += quantidade
        else:
            print("Quantidade de ingressos indisponível.")

    elif menu == 6:
        sala = "F3_S2"
        exibir_poltronas(sala)
        info(filmes_assentos, "F3_S2", precos, 1, 6, 3)
        quantidade = int(input("Quantas poltronas deseja selecionar? "))
        poltronas_escolhidas = escolher_poltronas(sala, quantidade, poltronas)
        ingresso = int(input("Digite o número correspondente ao ingresso que você quer: "))

        if quantidade <= filmes_assentos["F3_S2"]:
            filmes_assentos["F3_S2"] -= quantidade
            if ingresso == 1:
                calculos(precos, 1, qtd_ingressos, valores_arrecadados, "F3_S2", "Inteira", quantidade)
            elif ingresso == 2:
                calculos(precos, 6, qtd_ingressos, valores_arrecadados, "F3_S2", "Meia", quantidade)
            elif ingresso == 3:
                calculos(precos, 3, qtd_ingressos, valores_arrecadados, "F3_S2", "VIP", quantidade)
            else:
                print("Tipo de ingresso inválido.")
                filmes_assentos["F3_S2"] += quantidade
        else:
            print("Quantidade de ingressos indisponível.")

    elif menu == 7:
        print("\n AVALIAÇÃO")
        print("\n 1. Filme 1 \n 2. Filme 2 \n 3. Filme 3")
        filme = int(input("Digite o número correspondente ao filme que você quer avaliar: "))

        if filme == 1:
            nota = int(input("Dê uma nota de 1 a 5 para o Filme: "))
            avaliacao(avaliacoes, nota, "F1")
        elif filme == 2:
            nota = int(input("Dê uma nota de 1 a 5 para o Filme: "))
            avaliacao(avaliacoes, nota, "F2")
        elif filme == 3:
            nota = int(input("Dê uma nota de 1 a 5 para o Filme: "))
            avaliacao(avaliacoes, nota, "F3")

    elif menu == 8:
        break

    else:
        print("Opção inválida")

print("\nRELATÓRIO FINAL\n")
for filme in ["F1", "F2", "F3"]:
    for sessao in ["S1", "S2"]:
        chave = f"{filme}_{sessao}"
        print(f"\n{filme} - {sessao}")
        print("\n  Quantidade de ingressos vendidos:")
        print(f"    - Inteiras: {qtd_ingressos[chave]['Inteira']}")
        print(f"    - Meia Entrada: {qtd_ingressos[chave]['Meia']}")
        print(f"    - VIP: {qtd_ingressos[chave]['VIP']}")
        print("\n  Receita total do dia POR TIPO:")
        print(f"    - Inteira: R${valores_arrecadados[chave]['Inteira']:.2f}")
        print(f"    - Meia Entrada: R${valores_arrecadados[chave]['Meia']:.2f}")
        print(f"    - VIP: R${valores_arrecadados[chave]['VIP']:.2f}\n")

print("\n \nTotal de ingressos vendidos: {}".format(sum(total_qtd_ingressos)))
print("Receita total do dia: R${:.2f}".format(sum(receita_total_dia)))

print("\nMÉDIAS DAS AVALIAÇÕES")
for filme in ["F1", "F2", "F3"]:
    if avaliacoes[filme]["quantidade"] > 0:
        media = avaliacoes[filme]["notas"] / avaliacoes[filme]["quantidade"]
        avaliacoes[filme]["notas"] = media #Substitui o valor da nota pela media apos a conta
    else:
        media = 0
    print(f"  {filme}: {media:.1f}")

print("\nGRÁFICO DE AVALIAÇÕES")    
grafico_barra([int(avaliacoes[filme]["notas"]) for filme in ["F1", "F2", "F3"]])
