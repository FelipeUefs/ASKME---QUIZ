#/*******************************************************************************
#Autor: Felipe Gomes da Silva
#Componente Curricular: Algoritmos I
#Concluido em: 08/12/2024
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/
#SISTEMA OPERACIONAL: WINDOWS 10
#VERSÃO DO PYTHON: 3.13.0

#BLOCO 1 - MENUS E BIBLIOTECAS
import time
import os
import json
import random

#MENU DE JOGO
def modo_jogo(menu):
    if menu == 1:
        jogo1("quiz1.json")
    elif menu == 2:
        jogo2("quiz1.json")
    elif menu == 3:
        jogo3("quiz1.json")
    elif menu == 4:
        menuhall("hall")
    elif menu == 5:
        print("OBRIGADO POR JOGAR!")

#MENU DO HALL DA FAMA
def menuhall(hall):
    h = "S"
    while h == "S":
        limpeza()
        hall = int(input("QUAL HALL DESEJA VISITAR?"
                     "\n[1] HALL QUESTÕES FIXAS\n[2] HALL CONTRA O TEMPO\n[3] HALL HARDCORE\n[4] PARA VOLTAR\n"))
        if hall == 1:
           exibihall1("hall1")
        elif hall == 2:
            exibihall2("hall2")
        elif hall == 3:
            exibihall3("hall3")
        elif hall == 4:
            print("Voltando ao menu...")
            time.sleep(1)
            break
#FIM DO BLOCO 1

#BLOCO 2 - EXIBIÇÃO 
#EXIBIÇÃO DO hall1
def exibihall1(hall1):
        try: #Se o arquivo existir ele abre 
            with open("hall_qfixas.json", "r", encoding= "utf-8") as hall1:
                linhas = json.load(hall1)
                hall_organizado1 = sorted(linhas.items(), key=lambda x: x[1], reverse=True)[:10]
                limpeza()
                print(f"{"":^3}HALL DA FAMA DE QUESTÕES FIXAS\n")
                print(f"{"COLOCAÇÃO":<12}{"JOGADOR":<12}{"PONTOS":<10}")
                for i,(nome, pontos) in enumerate(hall_organizado1,1):
                    print(f"{i}°{"":<9} {nome:<11} {pontos} pontos {"":<7}")
                time.sleep(5)
        except FileNotFoundError:
            print("\nNão Existe Hall registrado")
            time.sleep(3)

#EXIBIÇÃO DO HALL2
def exibihall2(hall2):
    try:
        with open("hall_contratempo.json", "r", encoding= "utf-8") as hall2:
                    linhas = json.load(hall2)
                    hall_organizado2 = sorted(linhas.items(), key=lambda x: x[1], reverse=True)[:10]
                    limpeza()
                    print(f"{"":^3}HALL DA FAMA CONTRA O TEMPO\n")
                    print(f"{"COLOCAÇÃO":<10}{"JOGADOR":<10}{"FINALIZOU FALTANDO":<10}")
                    for i,(nome, tempo) in enumerate(hall_organizado2,1):
                        print(f"{i}°{"":<7} {nome:<10} {tempo} segundos{"":<7} ")
                    time.sleep(5)
    except FileNotFoundError:
            print("\nNão Existe Hall registrado")
            time.sleep(3)

#EXIBIÇÃO DO HALL3
def exibihall3(hall3):
    try:
        with open("hall_hardcore.json", "r", encoding= "utf-8") as hall3:
                    linhas = json.load(hall3)
                    hall_organizado3 = sorted(linhas.items(), key=lambda x: x[1], reverse=True)[:10]
                    limpeza()
                    print(f"{"":^3}HALL DA FAMA HARDCORE\n")
                    print(f"{"COLOCAÇÃO":<10}{"JOGADOR":<10}{"ACERTADAS":<10}")
                    for i,(nome, pontos) in enumerate(hall_organizado3,1):
                        print(f"{i}°{"":<7} {nome:<10} {pontos} Questões{"":<7}")
                    time.sleep(5)
    except FileNotFoundError:
            print("\nNão Existe Hall registrado")
            time.sleep(3)

#EXIBIR AS ALTERNATIVAS
def exibir_questoes(alterna):
    for op, opçoes in enumerate(alterna, 1):
                print(f"{op} : {opçoes}")

#LIMPEZA DE TELA
def limpeza():
    if os.name == "nt":
        os.system("cls")
#FIM DO BLOCO 2

#BLOCO 3 - SALVAR ARQUIVOS E SORTEIO DE DICAS
#DICAS
def dicas(A, B, C):
    #retorna quando uma das variaveis não seja 0.
    #if A != 0 and B != 0 and C != 0:
            #return dicas(A, B, C)
    #VERIFICA SE A VARIAVEL É 0, SE FOR ELE ADICIONA NA SORTEADA E SAI DO LOOPING.
    while A == 0 or B == 0 or C == 0:
        sort_dicas = random.choice([1,2,3])
        if sort_dicas == 1 and A == 0:
            A += 1
            break
        elif sort_dicas == 2 and B == 0:
            B += 1
            break
        elif sort_dicas == 3 and C == 0:
            C += 1
            break
    return A, B, C

#ADICIONAR NOMES NO HALL1
def halljogo1(nome, pontos):
    try: #Se o arquivo existir ele abre 
        with open("hall_qfixas.json", "r", encoding="utf-8") as hall1:
            hall_um = json.load(hall1)
    #ABRE O ARQUIVO PARA Adicionar no hall e organizar
    except FileNotFoundError: 
        hall_um = {}
    hall_um[nome] = pontos #chave e valor do dicionario 
    hall_organizado = sorted(hall_um.items(), key=lambda x: x[1], reverse=True)#organiza o hall da fama
    with open("hall_qfixas.json", "w", encoding= "utf-8") as hall1:
        json.dump(dict(hall_organizado), hall1, indent=4)
    print("ATUALIZAÇÃO DE HALL COMPLETA!")
    exibir = input("Deseja ver o Hall?[S/N]").strip().upper()
    if exibir == "S":
        exibihall1("hall1")
    else: 
        print("ATUALIZAÇÃO DE HALL COMPLETA!")

#ADICIONAR NOMES NO HALL2
def halljogo2(nome, tempo):
    try:
        with open("hall_contratempo.json", "r", encoding="utf-8") as hall2:
                hall_dois = json.load(hall2)
    except FileNotFoundError:
    #ABRE O ARQUIVO PARA Adicionar no hall e organizar 
            hall_dois = {}
    hall_dois[nome] = tempo
    hall_organizado = sorted(hall_dois.items(), key=lambda x: x[1], reverse=True)
    with open("hall_contratempo.json", "w", encoding= "utf-8") as hall1:
        json.dump(dict(hall_organizado), hall1, indent=4)
    print("ATUALIZAÇÃO DE HALL COMPLETA!")
    exibir = input("Deseja Exibir o Hall? [S/N]").strip().upper()
    if exibir == "S":
            exibihall2("hall2")
    else: 
        print("ATUALIZAÇÃO DE HALL COMPLETA!")

#ADICIONAR NOMES NO HALL3
def halljogo3(nome, acumula):
    try:
        with open("hall_hardcore.json", "r", encoding="utf-8") as hall1:
            hall_tres = json.load(hall1)
    #ABRE O ARQUIVO PARA Adicionar no hall e organizar 
    except FileNotFoundError:
        hall_tres = {}
    hall_tres[nome] = acumula
    hall_organizado = sorted(hall_tres.items(), key=lambda x: x[1], reverse=True)
    with open("hall_hardcore.json", "w", encoding= "utf-8") as hall1:
        json.dump(dict(hall_organizado), hall1, indent=4)
    print("ATUALIZAÇÃO DE HALL COMPLETA!")
    exibir = input("Deseja Exibir o Hall? [S/N]").strip().upper()
    if exibir == "S":
        exibihall3("hall3")
    else: 
        print("ATUALIZAÇÃO DE HALL COMPLETA!")
#FIM DO BLOCO 3

#BLOCO 4 - MODOS DE JOGO
#DEFINIÇÃO DO JOGO 1
def jogo1(arquivo):
    limpeza()
    print("VAMOS JOGAR!\nSE PREPARE!")
    for conta in range(3,-1,-1):
        print(conta)
        time.sleep(0.5)
    #ABRE O ARQUIVO PARA LEITURA
    with open("quiz1.json", "r", encoding= "utf-8") as arquivo:
        quiz = json.load(arquivo)
        pontos = 0 #PONTOS DO JOGO
        p = random.sample(quiz, 20)
        acumula = 0
        dica_exp = 1
        pular = 1
        eliminar = 1
        respondidas = []
        #PUXA O DICIONARIO DO ARQUIVO JSON
        for pergunta in p:
            categoria = pergunta["category"]
            valor = pergunta["value"]
            questao = pergunta["questionText"]
            alterna = [pergunta["option1"],pergunta["option2"],pergunta["option3"],pergunta["option4"],pergunta["option5"]]
            correta = pergunta["answer"][-1]
            explica = pergunta["explanation"]
            dica =  pergunta["hint"]
            limpeza()
            if questao in respondidas:
                continue
            else: 
                #EXIBE NA TELA
                print(f"\nCategoria : {categoria}\t Valor: {valor}")
                print(f"Pontos acumulados {pontos}")
                print(f"\nQuestão: {questao}")
                #EXIBIR AS QUESTÕES
                exibir_questoes(alterna)
                #VERIFICAÇÃO DE ERRO DE DIGITAÇÃO
                validas = ["1","2","3","4","5","A", "B", "C", "S"]
                while True:
                    try:
                        print("\nDIGITE SUA RESPOSTA OU ESCOLHA UMA AJUDA DIGITANDO:\n"
                                f"A - EXIBIR DICA {dica_exp}\tB - PULAR QUESTÃO {pular}\tC - ELIMINAR 3 ALTERNATIVAS ERRADAS {eliminar}\tS - PARA VOLTAR AO MENU\n")
                        jogador = input("Sua Resposta: ").strip().upper()
                        if jogador in validas:
                            break
                        else: 
                            raise ValueError ("Insira valores validos! Escolha de 1-5 ou A-C ou S")
                    except ValueError as e: 
                        print(e)
                if jogador == correta:
                    print('Resposta Correta!')
                    time.sleep(1)
                    respondidas.append(questao)
                    pontos += int(valor)
                    acumula += 1
                    if acumula == 6:
                        dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                elif jogador == "A":
                    if dica_exp == 1:
                        print(f"Dica: {dica}")
                        dica_exp -= 1
                        jogador = input("Sua Resposta: ").strip().upper()
                        if jogador == correta:
                            print('Resposta Correta!')
                            time.sleep(1)
                            respondidas.append(questao)
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar) 
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(4)
                    else:
                        print("DICA INDISPONIVEL")
                        jogador = input('Sua Resposta: ').strip()
                        if jogador == correta:
                            print('Resposta Correta!')
                            time.sleep(1)
                            respondidas.append(questao)
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(4)
                #PULA A QUESTÃO
                elif jogador == "B":
                    if pular == 1:
                        print("Questão pulada! ")
                        pular -= 1
                        dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        continue
                    else:
                        print("DICA INDISPONIVEL!")
                        jogador = input('Sua Resposta: ').strip()
                        if jogador == correta:
                            print('Resposta Correta!')
                            time.sleep(1)
                            respondidas.append(questao)
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(4)
                #RETIRA 3 QUESTÕES ERRADAS DAS ALTERNATIVAS
                elif jogador == "C":
                    if eliminar == 1:
                        alternativas = {"option1": pergunta["option1"], "option2": pergunta["option2"], "option3": pergunta["option3"],
                                        "option4": pergunta["option4"], "option5": pergunta["option5"]}
                        alter_erradas = [i for i, opcao in alternativas.items() if i != pergunta["answer"]]
                        retiradas = random.sample(alter_erradas, 3)
                        for r in retiradas:
                            alternativas[r] = ""
                        print("Alternativas Erradas retiradas!")
                        time.sleep(1)
                        limpeza()
                        #Exibe as novas alternativas e a QUESTÃO
                        print(f"\nCategoria : {categoria}\t Valor: {valor}")
                        print(f"Pontos acumulados {pontos}")
                        print(f"Questão: {questao}")
                        for r, (chave, opçao) in enumerate(alternativas.items(), 1):
                            if opçao != "":
                                print(f"{r} : {opçao}")
                        eliminar -= 1
                        jogador = input('Sua Resposta: ').strip()
                        if jogador == correta:
                            print('Resposta Correta!')
                            time.sleep(1)
                            respondidas.append(questao)
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(4)   
                    else:
                        print("DICA INDISPONIVEL!")
                        jogador = input('Sua Resposta: ').strip()
                        if jogador == correta:
                            print('Resposta Correta!')
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(4)
                elif jogador == "S":
                    print("Voltando ao menu principal...")
                    break
                #RESPOSTA DO USUÁRIO
                else:
                    print("\nReposta Incorreta")
                    print(f"\nExplicação: {explica}")
                    time.sleep(4)
        time.sleep(3)
        limpeza()
        print("FIM do JOGO")
        print(f"Sua pontuação: {pontos} pontos")
        nome = input("\nDigite seu nome: ").strip()
        halljogo1(nome,pontos)
        print("ATÉ A PROXIMA!")         

#DEFINIÇÃO JOGO 2
def jogo2(arquivo):
    limpeza()
    print("VAMOS JOGAR!\nSE PREPARE!")
    for conta in range(3,-1,-1):
        print(conta)
        time.sleep(0.5)
    with open("quiz1.json", "r", encoding= "utf-8") as arquivo:
        quiz = json.load(arquivo)
        pontos = 0 #PONTOS DO JOGO
        acumula = 0
        dica_exp = 1
        pular = 1
        eliminar = 1
        respondidas = []
        #EXIBE NA TELA
        tempo = time.time()
        limite_T = tempo + 300  #300 segundos (5 minutos)
        while time.time() < limite_T :  #Limpa a tela
            p = random.sample(quiz, 20)
            for pergunta in p:
                #PUXA O DICIONARIO DO ARQUIVO JSON
                categoria = pergunta["category"]
                valor = pergunta["value"]
                questao = pergunta["questionText"]
                alterna = [pergunta["option1"],pergunta["option2"],pergunta["option3"],pergunta["option4"],pergunta["option5"]]
                correta = pergunta["answer"][-1]
                explica = pergunta["explanation"]
                dica =  pergunta["hint"]
            restante = int(limite_T - time.time())
            time.sleep(1)
            limpeza()
            if questao in respondidas:
                continue
            else:
                #EXIBIR AS QUESTÕES
                print(f"\n\rCategoria : {categoria}\t Valor: {valor} Tempo: {restante}")
                print(f"Pontos acumulados {pontos}")
                print(f"\nQuestão: {questao}")
                exibir_questoes(alterna)
                #DICAS
                validas = ["1","2","3","4","5","A", "B", "C", "S"]
                while True:
                    try:
                        print("\nDIGITE SUA RESPOSTA OU ESCOLHA UMA AJUDA DIGITANDO:\n"
                                f"A - EXIBIR DICA {dica_exp}\tB - PULAR QUESTÃO {pular}\tC - ELIMINAR 3 ALTERNATIVAS ERRADAS {eliminar}\tS - PARA VOLTAR AO MENU\n")
                        jogador = input("Sua Resposta: ").strip().upper()
                        if jogador in validas:
                            break
                        else:
                            raise ValueError ("Insira valores validos! Escolha de 1-5 ou A-C ou S")
                            
                    except ValueError as e: 
                        print(e) 
                if jogador == correta:
                    print('Resposta Correta!')
                    time.sleep(1)
                    respondidas.append(questao)
                    pontos += int(valor)
                    acumula += 1
                    if acumula == 6:
                        dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                elif jogador == "A":
                    if dica_exp == 1:
                        print(f"Dica: {dica}")
                        dica_exp -= 1
                        jogador = input("Sua Resposta: ").strip().upper()
                        if jogador == correta:
                            print('Resposta Correta!')
                            time.sleep(1)
                            respondidas.append(questao)
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(1)
                    else:
                        print("DICA INDISPONIVEL")
                        jogador = input('Sua Resposta: ').strip()
                        if jogador == correta:
                            print('Resposta Correta!')
                            time.sleep(1)
                            respondidas.append(questao)
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(1)
                #PULA A QUESTÃO
                elif jogador == "B":
                    if pular == 1:
                        print("Questão pulada! ")
                        pular -= 1
                        continue
                    else:
                        print("DICA INDISPONIVEL!")
                        jogador = input('Sua Resposta: ').strip()
                        if jogador == correta:
                            print('Resposta Correta!')
                            time.sleep(1)
                            respondidas.append(questao)
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(1)
                #RETIRA 3 QUESTÕES ERRADAS DAS ALTERNATIVAS
                elif jogador == "C":
                    if eliminar == 1:
                        alternativas = {"option1": pergunta["option1"], "option2": pergunta["option2"], "option3": pergunta["option3"],
                                        "option4": pergunta["option4"], "option5": pergunta["option5"]}
                        alter_erradas = [i for i, opcao in alternativas.items() if i != pergunta["answer"]]
                        retiradas = random.sample(alter_erradas, 3)
                        for r in retiradas:
                            alternativas[r] = ""
                        print("Alternativas Erradas retiradas!")
                        #Exibe as novas alternativas
                        time.sleep(1)
                        limpeza()
                        #EXIBIR AS QUESTÕES
                        print(f"\n\rCategoria : {categoria}\t Valor: {valor} Tempo: {restante}")
                        print(f"Pontos acumulados {pontos}")
                        print(f"Questão: {questao}")
                        for r, (chave, opçao) in enumerate(alternativas.items(), 1):
                            if opçao != "":
                                print(f"{r} : {opçao}")
                        eliminar -= 1
                        jogador = input('Sua Resposta: ').strip()
                        if jogador == correta:
                            print('Resposta Correta!')
                            time.sleep(1)
                            respondidas.append(questao)
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(1)
                    else:
                        print("DICA INDISPONIVEL!")
                        jogador = input('Sua Resposta: ').strip()
                        if jogador == correta:
                            print('Resposta Correta!')
                            time.sleep(1)
                            respondidas.append(questao)
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(1)         
                elif jogador == "S":
                    print("Voltando ao menu principal...")
                    break
                #RESPOSTA DO USUÁRIO
                else:
                    print("\nReposta Incorreta")
                    print(f"\nExplicação: {explica}")
                    time.sleep(1)
        if restante == 0:
            limpeza()
        time.sleep(1)
        limpeza() 
        print("FIM do JOGO")
        print(f"Sua pontuação: {pontos} pontos")
        print(f"Seu tempo foi: {restante}")
        nome = input("Digite seu nome: ").strip()
        print("ATÉ A PROXIMA!")
        halljogo2(nome,restante)

#DEFINIÇÃO JOGO 3           
def jogo3(arquivo):
    limpeza()
    print("VAMOS JOGAR!\nSE PREPARE!")
    for conta in range(3,-1,-1):
        print(conta)
        time.sleep(0.5)
    with open("quiz1.json", "r", encoding= "utf-8") as arquivo:
        quiz = json.load(arquivo)
        pontos = 0 #PONTOS DO JOGO
        p = random.sample(quiz,25)
        acumula = 0
        dica_exp = 1
        pular = 1
        eliminar = 1
        respondidas = []
        limpeza()
        #PUXA O DICONARIO DO ARQUIVO JSON
        for pergunta in p:
            categoria = pergunta["category"]
            valor = pergunta["value"]
            questao = pergunta["questionText"]
            alterna = [pergunta["option1"],pergunta["option2"],pergunta["option3"],pergunta["option4"],pergunta["option5"]]
            correta = pergunta["answer"][-1]
            explica = pergunta["explanation"]
            dica =  pergunta["hint"]
            time.sleep(1)
            limpeza()
            if questao in respondidas:
                continue
            else:
                #EXIBE NA TELA 
                print(f"\nCategoria : {categoria}\t Valor: {valor}")
                print(f"Questões Acertadas: {acumula}\t Pontos: {pontos}")
                print(f"Questão: {questao}")
                #EXIBIR AS QUESTÕES
                exibir_questoes(alterna)
                #DICAS
                validas = ["1","2","3","4","5","A", "B", "C", "S"]
                while True:
                    try:
                        print("\nDIGITE SUA RESPOSTA OU ESCOLHA UMA AJUDA DIGITANDO:\n"
                                f"A - EXIBIR DICA: {dica_exp}\tB - PULAR QUESTÃO: {pular}\tC - ELIMINAR 3 ALTERNATIVAS ERRADAS: {eliminar}\tS - PARA VOLTAR AO MENU\n")
                        jogador = input("Sua Resposta: ").strip().upper()
                        if jogador in validas:
                            break
                        else: 
                            raise ValueError ("Insira valores validos! Escolha de 1-5 ou A-C ou S")
                    except ValueError as e: 
                        print(e) 
                if jogador == correta:
                    print('Resposta Correta!')
                    time.sleep(1)
                    respondidas.append(questao)
                    pontos += int(valor)
                    acumula += 1
                    if acumula == 6:
                        dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                elif jogador == "A":
                    if dica_exp == 1:
                        print(f"Dica: {dica}")
                        dica_exp -= 1
                        jogador = input('Sua Resposta: ').strip()
                        if jogador == correta:
                            print('Resposta Correta!')
                            time.sleep(1)
                            respondidas.append(questao)
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(4)
                            break
                    else:
                        print("DICA INDISPONIVEL")
                        jogador = input('Sua Resposta: ').strip()
                        if jogador == correta:
                            print('Resposta Correta!')
                            time.sleep(1)
                            respondidas.append(questao)
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(4)
                            break
                #PULA A QUESTÃO
                elif jogador == "B":
                    if pular == 1:
                        print("Questão pulada! ")
                        pular -= 1
                        continue
                    else:
                        print("DICA INDISPONIVEL!")
                        jogador = input('Sua Resposta: ').strip()
                        if jogador == correta:
                            print('Resposta Correta!')
                            time.sleep(1)
                            respondidas.append(questao)
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(4)
                            break
                #RETIRA 3 QUESTÕES ERRADAS DAS ALTERNATIVAS
                elif jogador == "C":
                    if eliminar == 1:
                        alternativas = {"option1": pergunta["option1"], "option2": pergunta["option2"], "option3": pergunta["option3"],
                                        "option4": pergunta["option4"], "option5": pergunta["option5"]}
                        alter_erradas = [i for i, opcao in alternativas.items() if i != pergunta["answer"]]
                        retiradas = random.sample(alter_erradas, 3)
                        for r in retiradas:
                            alternativas[r] = ""
                        print("Alternativas Erradas retiradas!")
                        #EXIBE A QUESTÃO
                        time.sleep(1)
                        limpeza()
                        print(f"\nCategoria : {categoria}\t Valor: {valor}")
                        print(f"Questões Acertadas: {acumula}\t Pontos: {pontos}")
                        print(f"Questão: {questao}")
                        #EXIBIR AS ALTERNATIVAS
                        eliminar -= 1
                        for r, (chave, opçao) in enumerate(alternativas.items(), 1):
                            if opçao != "":
                                print(f"{r} : {opçao}")
                        #RESPOSTA DO USUÁRIO
                        jogador = input('Sua Resposta: ').strip()
                        if jogador == correta:
                            print('Resposta Correta!')
                            time.sleep(1)
                            respondidas.append(questao)
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(4)
                            break
                    else:
                        print("DICA INDISPONIVEL!")
                        jogador = input('Sua Resposta: ').strip()
                        if jogador == correta:
                            print('Resposta Correta!')
                            time.sleep(1)
                            respondidas.append(questao)
                            pontos += int(valor)
                            acumula += 1
                            if acumula == 6:
                                dica_exp, pular, eliminar = dicas(dica_exp, pular, eliminar)
                        else:
                            print("\nReposta Incorreta")
                            print(f"\nExplicação: {explica}")
                            time.sleep(4)
                            break
                elif jogador == "S":
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("\nReposta Incorreta")
                    print(f"\nExplicação: {explica}")
                    time.sleep(4)
                    break
        time.sleep(1)
        limpeza()
        print("FIM do JOGO")
        print(f"Sua pontuação: {pontos} pontos")
        print(f"Você acertou {acumula} questões")
        nome = input("Digite seu nome: ").strip()
        halljogo3(nome,acumula)
        print("ATÉ A PROXIMA!")
#FIM DO BLOCO 4

#BLOCO 5 -CODIGO PRINCIPAL
menu = 0
while menu != 5:
    limpeza()
    print("\nASKME")
    print("MENU PRINCIPAL")
    menu = int(input("Selecione a opção: "
                     "\n[1] Questões Fixas"
                     "\n[2] Contra o Tempo"
                     "\n[3] Hardcore"
                     "\n[4] Hall da Fama"
                     "\n[5] Encerrar\n"))
    modo_jogo(menu)   