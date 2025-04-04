#Isaac Koga - 10723323

preco_filme = [20,15,10]     #lista de preços por filme
cont_poltronas = [0,0,0,0,0,0]     #contador de assentos disponiveis
poltrona_f1 = ['D']*50       #capacidade por filme
poltrona_f2 = ['D']*40
poltrona_f3 = ['D']*30
cont_int = [0,0,0,0,0,0]   # Inicialização de Contadores de Ingressos Vendidos por tipo para cada sessão de cada filme [f1s1, f1s2, f2s1, f2s2, f3s1,...]
cont_meia = [0,0,0,0,0,0]
cont_vip = [0,0,0,0,0,0]
total_iv11 = cont_int[0] + cont_meia[0] + cont_vip[0]
total_iv12 = cont_int[1] + cont_meia[1] + cont_vip[1]  
total_iv21 = cont_int[2] + cont_meia[2] + cont_vip[2]
total_iv22 = cont_int[3] + cont_meia[3] + cont_vip[3]
total_iv31 = cont_int[4] + cont_meia[4] + cont_vip[4]
total_iv32 = cont_int[5] + cont_meia[5] + cont_vip[5]


'''
# Inicialização de Avaliações e de seu Total em Quantidade (por Filme)
av_f1=0
av_f2=0
av_f3=0
total_av_f1=0      
total_av_f2=0
total_av_f3=0'''

def menu():
    print ("\n---------------------------MENU--------------------------")
    print ("| 1 - Filme 1 (primeira sessão) - Comprar ingressos	|")
    print ("| 2 - Filme 1 (segunda sessão) - Comprar ingressos	|")
    print ("| 3 - Filme 2 (primeira sessão) - Comprar ingressos	|")
    print ("| 4 - Filme 2 (segunda sessão) - Comprar ingressos	|")
    print ("| 5 - Filme 3 (primeira sessão) - Comprar ingressos	|")
    print ("| 6 - Filme 3 (segunda sessão) - Comprar ingressos	|")
    print ("| 7 - Avaliar um filme		    			|")
    print ("| 8 - Encerrar o dia e exibir relátorio			|")
    print ("---------------------------------------------------------")
    op = int(input("Escolha uma das opções: "))
    while op<1 or op>8:                               #Validaçao da entrada da opção
        op = int(input("Opção inválida, digite novamente (1 a 8): ")) 
    return op

def venda():
    

def main():
    while True:
        op = menu()
        if op == 8:
            break
        if op == 1:
            venda_()
        if op == 2:
            menu()
        if op == 3:
            menu()
        if op == 4:
            menu()
        if op == 5:
            menu()
        if op == 6:
            menu()
        if op == 7:
            menu()
    

'''

    if op == 1:                             

        while True: 

            if total_iv11 == cap11:
                print()
                print("Agora não há mais ingressos disponíveis para essa sessão.")
                break

            print (" ")    
            print (f"Há {cap11-total_iv11} ingressos disponíveis para o Filme 1 - Sessão 1")
            print (" ") 
            print ("--------------------------")
            print ("| 1 - Ingresso Inteira   |")
            print ("| 2 - Ingresso Meia      |")
            print ("| 3 - Ingresso VIP       |")
            print ("| 4 - Voltar             |")
            print ("--------------------------")

            op_ing = int (input ("Escolha uma das opções: ")) 
            while op_ing<1 or op_ing>4:                                               #Validaçao da entrada da opção
                op_ing = int(input("Opção inválida, digite novamente (1 a 4): ")) 

            if op_ing == 1:
                qtd = int(input("Quantos ingressos inteira deseja comprar? "))
                if qtd <= cap11-total_iv11:
                    iv_int11 += qtd
                    cap11 -= qtd
                    preco = qtd*pf1
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 2:
                qtd = int(input("Quantos ingressos meia deseja comprar? "))
                if qtd <= cap11-total_iv11:
                    iv_meia11 += qtd
                    cap11 -= qtd
                    preco = qtd*pf1*0.5
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 3:
                qtd = int(input("Quantos ingressos VIP deseja comprar? "))
                if qtd <= cap11-total_iv11:
                    iv_vip11 += qtd
                    cap11 -= qtd
                    preco = qtd*pf1*1.5
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 4:
                break

    elif op == 2:                             

        while True: 

            if total_iv12 == cap12:
                print()
                print("Agora não há mais ingressos disponíveis para essa sessão.")
                break

            print (" ")    
            print (f"Há {cap12-total_iv12} ingressos disponíveis para o Filme 1 - Sessão 2")
            print (" ") 
            print ("--------------------------")
            print ("| 1 - Ingresso Inteira   |")
            print ("| 2 - Ingresso Meia      |")
            print ("| 3 - Ingresso VIP       |")
            print ("| 4 - Voltar             |")
            print ("--------------------------")

            op_ing = int (input ("Escolha uma da opções: "))
            while op_ing<1 or op_ing>4:                                               #Validaçao da entrada da opção
                op_ing = int(input("Opção inválida, digite novamente (1 a 4): ")) 


            if op_ing == 1:
                qtd = int(input("Quantos ingressos inteira deseja comprar? "))
                if qtd <= cap12-total_iv12:
                    iv_int12 += qtd
                    cap12 -= qtd
                    preco = qtd*pf1
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 2:
                qtd = int(input("Quantos ingressos meia deseja comprar? "))
                if qtd <= cap12-total_iv12:
                    iv_meia12 += qtd
                    cap12 -= qtd
                    preco = qtd*pf1*0.5
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 3:
                qtd = int(input("Quantos ingressos VIP deseja comprar? "))
                if qtd <= cap12-total_iv12:
                    iv_vip12 += qtd
                    cap12 -= qtd
                    preco = qtd*pf1*1.5
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 4:
                break

    elif op == 3:                             

        while True: 

            if total_iv21 == cap21:
                print()
                print("Agora não há mais ingressos disponíveis para essa sessão.")
                break

            print (" ")    
            print (f"Há {cap21-total_iv21} ingressos disponíveis para o Filme 2 - Sessão 1")
            print (" ") 
            print ("--------------------------")
            print ("| 1 - Ingresso Inteira   |")
            print ("| 2 - Ingresso Meia      |")
            print ("| 3 - Ingresso VIP       |")
            print ("| 4 - Voltar             |")
            print ("--------------------------")

            op_ing = int (input ("Escolha uma da opções: ")) 
            while op_ing<1 or op_ing>4:                                               #Validaçao da entrada da opção
                op_ing = int(input("Opção inválida, digite novamente (1 a 4): ")) 

            if op_ing == 1:
                qtd = int(input("Quantos ingressos inteira deseja comprar? "))
                if qtd <= cap21-total_iv21:
                    iv_int21 += qtd
                    cap21 -= qtd
                    preco = qtd*pf2
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 2:
                qtd = int(input("Quantos ingressos meia deseja comprar? "))
                if qtd <= cap21-total_iv21:
                    iv_meia21 += qtd
                    cap21 -= qtd
                    preco = qtd*pf2*0.5
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 3:
                qtd = int(input("Quantos ingressos VIP deseja comprar? "))
                if qtd <= cap21-total_iv21:
                    iv_vip21 += qtd
                    cap21 -= qtd
                    preco = qtd*pf2*1.5
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 4:
                break

    elif op == 4:                             

        while True: 

            if total_iv22 == cap22:
                print()
                print("Agora não há mais ingressos disponíveis para essa sessão.")
                break

            print (" ")    
            print (f"Há {cap22-total_iv22} ingressos disponíveis para o Filme 2 - Sessão 2")
            print (" ") 
            print ("--------------------------")
            print ("| 1 - Ingresso Inteira   |")
            print ("| 2 - Ingresso Meia      |")
            print ("| 3 - Ingresso VIP       |")
            print ("| 4 - Voltar             |")
            print ("--------------------------")

            op_ing = int (input ("Escolha uma da opções: ")) 
            while op_ing<1 or op_ing>4:                                               #Validaçao da entrada da opção
                op_ing = int(input("Opção inválida, digite novamente (1 a 4): ")) 

            if op_ing == 1:
                qtd = int(input("Quantos ingressos inteira deseja comprar? "))
                if qtd <= cap22-total_iv22:
                    iv_int22 += qtd
                    cap21 -= qtd
                    preco = qtd*pf2
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 2:
                qtd = int(input("Quantos ingressos meia deseja comprar? "))
                if qtd <= cap22-total_iv22:
                    iv_meia22 += qtd
                    cap22 -= qtd
                    preco = qtd*pf2*0.5
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 3:
                qtd = int(input("Quantos ingressos VIP deseja comprar? "))
                if qtd <= cap22-total_iv22:
                    iv_vip22 += qtd
                    cap22 -= qtd
                    preco = qtd*pf2*1.5
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 4:
                break

    elif op == 5:                             

        while True: 

            if total_iv31 == cap31:
                print()
                print("Agora não há mais ingressos disponíveis para essa sessão.")
                break

            print (" ")    
            print (f"Há {cap31-total_iv31} ingressos disponíveis para o Filme 3 - Sessão 1")
            print (" ") 
            print ("--------------------------")
            print ("| 1 - Ingresso Inteira   |")
            print ("| 2 - Ingresso Meia      |")
            print ("| 3 - Ingresso VIP       |")
            print ("| 4 - Voltar             |")
            print ("--------------------------")

            op_ing = int (input ("Escolha uma da opções: ")) 
            while op_ing<1 or op_ing>4:                                               #Validaçao da entrada da opção
                op_ing = int(input("Opção inválida, digite novamente (1 a 4): ")) 


            if op_ing == 1:
                qtd = int(input("Quantos ingressos inteira deseja comprar? "))
                if qtd <= cap31-total_iv31:
                    iv_int31 += qtd
                    cap11 -= qtd
                    preco = qtd*pf3
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 2:
                qtd = int(input("Quantos ingressos meia deseja comprar? "))
                if qtd <= cap31-total_iv31:
                    iv_meia31 += qtd
                    cap31 -= qtd
                    preco = qtd*pf3*0.5
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 3:
                qtd = int(input("Quantos ingressos VIP deseja comprar? "))
                if qtd <= cap31-total_iv31:
                    iv_vip31 += qtd
                    cap31 -= qtd
                    preco = qtd*pf3*1.5
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 4:
                break

    elif op == 6:                             

        while True: 

            if total_iv32 == cap32:
                print()
                print("Agora não há mais ingressos disponíveis para essa sessão.")
                break

            print (" ")    
            print (f"Há {cap32-total_iv32} ingressos disponíveis para o Filme 3 - Sessão 2")
            print (" ") 
            print ("--------------------------")
            print ("| 1 - Ingresso Inteira   |")
            print ("| 2 - Ingresso Meia      |")
            print ("| 3 - Ingresso VIP       |")
            print ("| 4 - Voltar             |")
            print ("--------------------------")
            
            op_ing = int (input ("Escolha uma da opções: ")) 
            while op_ing<1 or op_ing>4:                                               #Validaçao da entrada da opção
                op_ing = int(input("Opção inválida, digite novamente (1 a 4): ")) 

            if op_ing == 1:
                qtd = int(input("Quantos ingressos inteira deseja comprar? "))
                if qtd <= cap32-total_iv32:
                    iv_int32 += qtd
                    cap11 -= qtd
                    preco = qtd*pf3
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 2:
                qtd = int(input("Quantos ingressos meia deseja comprar? "))
                if qtd <= cap32-total_iv32:
                    iv_meia32 += qtd
                    cap32 -= qtd
                    preco = qtd*pf3*0.5
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 3:
                qtd = int(input("Quantos ingressos VIP deseja comprar? "))
                if qtd <= cap32-total_iv32:
                    iv_vip32 += qtd
                    cap32 -= qtd
                    preco = qtd*pf3*1.5
                    print (f"Valor a ser pago: R${preco:.2f}")
                else:
                    print()
                    print("Não há essa quantidade de ingressos, confira novamente a disponibilidade:")
            elif op_ing == 4:
                break

    elif op == 7:
            print (" ")
            print ("---------Feedback---------")
            print ("| 1 - Avaliar Filme 1    |")
            print ("| 2 - Avaliar Filme 2    |")
            print ("| 3 - Avaliar Filme 3    |")
            print ("--------------------------")

            op_f = int(input('Escolha um filme para avaliar: '))
            while op_f<1 or op_f>3:                                               
                op_f = int(input("Opção inválida, digite novamente (1 a 3): ")) 
           
            if op_f == 1:
                nota = int(input('Avalie o filme de 1 a 5 estrelas: '))
                while nota<1 or nota>5:                                            
                    nota = int(input("Opção inválida, digite novamente (1 a 5): "))
                av_f1 += nota
                total_av_f1 += 1
            elif op_f == 2:
                nota = int(input('Avalie o filme de 1 a 5 estrelas: '))
                while nota<1 or nota>5:                                              
                    nota = int(input("Opção inválida, digite novamente (1 a 5): "))
                av_f2 += nota
                total_av_f2 += 1
            elif op_f == 3:
                nota = int(input('Avalie o filme de 1 a 5 estrelas: '))
                while nota<1 or nota>5:                                              
                    nota = int(input("Opção inválida, digite novamente (1 a 5): "))
                av_f3 += nota
                total_av_f3 += 1

    elif op == 8:

        total_iv11 = iv_int11 + iv_meia11 + iv_vip11
        total_iv12 = iv_int12 + iv_meia12 + iv_vip12      
        total_iv21 = iv_int21 + iv_meia21 + iv_vip21
        total_iv22 = iv_int22 + iv_meia22 + iv_vip22
        total_iv31 = iv_int31 + iv_meia31 + iv_vip31
        total_iv32 = iv_int32 + iv_meia32 + iv_vip32

        receita_meia11 = cont_meia[0] * (pf1/2)
        receita_int11 = iv_int11 * pf1
        receita_vip11 = iv_vip11 * (pf1*1.5)

        receita_meia12 = iv_meia12 * (pf1/2)
        receita_int12 = iv_int12 * pf1
        receita_vip12 = iv_vip12 * (pf1*1.5)

        receita_f1 = receita_meia11 + receita_int11 + receita_vip11 + receita_meia12 + receita_int12 + receita_vip12


        receita_meia21 = iv_meia21 * (pf2/2)
        receita_int21 = iv_int21 * pf2
        receita_vip21 = iv_vip21 * (pf2*1.5)

        receita_meia22 = iv_meia22 * (pf2/2)
        receita_int22 = iv_int22 * pf2
        receita_vip22 = iv_vip22 * (pf2*1.5)

        receita_f2 = receita_meia21 + receita_int21 + receita_vip21 + receita_meia22 + receita_int22 + receita_vip22


        receita_meia31 = iv_meia31 * (pf3/2)
        receita_int31 = iv_int31 * pf3
        receita_vip31 = iv_vip31 * (pf3*1.5)

        receita_meia32 = iv_meia32 * (pf3/2)
        receita_int32 = iv_int32 * pf3
        receita_vip32 = iv_vip32 * (pf3*1.5)

        receita_f3 = receita_meia31 + receita_int31 + receita_vip31 + receita_meia32 + receita_int32 + receita_vip32


        receita_total = receita_f1 + receita_f2 + receita_f3

        print (" ")
        print ("--------------------------Relatório Final------------------------")
        print ("| Filme 1 - Sessão 1:					    	|")
        print ("|-----------------Quantidade de ingressos vendidos--------------|")
        print (f"| Meia: {cont_meia[0]} - Receita: R${receita_meia11:.2f}			                |")
        print (f"| Inteira: {iv_int11} - Receita: R${receita_int11:.2f}			                |")
        print (f"| VIP: {iv_vip11} - Receita: R${receita_vip11:.2f}			                |")
        if total_av_f1 !=0:
            print (f"| Avaliação do Filme 1: {av_f1/total_av_f1:.1f}			                |")
        print ("-----------------------------------------------------------------")
        print ("| Filme 1 - Sessão 2:			                	|")
        print ("|-----------------Quantidade de ingressos vendidos--------------|")
        print (f"| Meia: {iv_meia12} - Receita: R${receita_meia12:.2f}			                |")
        print (f"| Inteira: {iv_int12} - Receita: R${receita_int12:.2f}			                |")
        print (f"| VIP: {iv_vip12} - Receita: R${receita_vip12:.2f}			                |")
        if total_av_f1 !=0:
            print (f"| Avaliação do Filme 1: {av_f1/total_av_f1:.1f}			                |")
        print ("-----------------------------------------------------------------")   
        print ("| Filme 2 - Sessão 1:			                	|")
        print ("|-----------------Quantidade de ingressos vendidos--------------|")
        print (f"| Meia: {iv_meia21} - Receita: R${receita_meia21:.2f}			                |")
        print (f"| Inteira: {iv_int21} - Receita: R${receita_int21:.2f}			                |")
        print (f"| VIP: {iv_vip21} - Receita: R${receita_vip21:.2f}			                |")
        if total_av_f2 !=0:
            print (f"| Avaliação do Filme 2:  {av_f2/total_av_f2:.1f}			                |")
        print ("-----------------------------------------------------------------")    
        print ("| Filme 2 - Sessão 2:			                	|")
        print ("|-----------------Quantidade de ingressos vendidos--------------|")
        print (f"| Meia: {iv_meia22} - Receita: R${receita_meia22:.2f}			                |")
        print (f"| Inteira: {iv_int22} - Receita: R$ {receita_int22:.2f}			                |")
        print (f"| VIP: {iv_vip22} - Receita: R${receita_vip22:.2f}			                |")
        if total_av_f2 !=0:
            print (f"| Avaliação do Filme 2:  {av_f2/total_av_f2:.1f}			                |")
        print ("-----------------------------------------------------------------")  
        print ("| Filme 3 - Sessão 1:			                	|")
        print ("|-----------------Quantidade de ingressos vendidos--------------|")
        print (f"| Meia: {iv_meia31} - Receita: R${receita_meia31:.2f}			                |")
        print (f"| Inteira: {iv_int31} - Receita: R${receita_int31:.2f}			                |")
        print (f"| VIP: {iv_vip31} - Receita: R${receita_vip31:.2f}			                |")
        if total_av_f3 !=0:
            print (f"| Avaliação do Filme 3: {av_f3/total_av_f3:.1f}			                |")
        print ("-----------------------------------------------------------------")   
        print ("| Filme 3 - Sessão 2:			                	|")
        print ("|-----------------Quantidade de ingressos vendidos--------------|")
        print (f"| Meia: {iv_meia32} - Receita: R${receita_meia32:.2f}			                |")
        print (f"| Inteira: {iv_int32} - Receita: R${receita_int32:.2f}			                |")
        print (f"| VIP: {iv_vip32} - Receita: R${receita_vip32:.2f}			                |")
        if total_av_f3 !=0:
            print (f"| Avaliação do Filme 3:  {av_f3/total_av_f3:.1f}			                |")
        print ("-----------------------------------------------------------------")  
        print (f"| Total de ingressos vendidos: {total_iv11 + total_iv12 + total_iv21 + total_iv22 + total_iv31 + total_iv32}		                |")
        print (f"| Receita do dia: R${receita_total:.2f}			                |")
        print ("-----------------------------------------------------------------")'''

main()
