# importei 2 bibliotecas, time pra dar delay e colorama pra deixar bonitinho
import time
from colorama import init, Fore
init()

# função que recebe as info e não aceita valores menores que 1 e maiores que 5
def inputValidator(aquiEuReceboAsInfo):
    while True:
        try:
            value = int(input(Fore.GREEN + aquiEuReceboAsInfo))
            if value >= 1 and value <= 5:
                return value
            else:
                print("Por favor, insira um número entre 1 e 5. vamos tentar novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número entre 1 e 5.")
            
# pura balaca pra fingir que ta carregando         
print(Fore.MAGENTA + "Aguarde, o Jogo está carregando...")
time.sleep(2)

# funcão que inicia o jogo
def gameInit():
    print(Fore.GREEN + "Olá! Bem-vindo ao jogo de carreira em tecnologia!")
    print(Fore.YELLOW + "Neste jogo, você responderá a algumas perguntas para descobrir qual área da tecnologia combina mais com você.")
    time.sleep(1)
    print(Fore.CYAN + """
    As áreas disponíveis são:
    - Desenvolvimento de Software
    - Área de Produtos (UX/UI, Product Owner, Product Manager, etc.)
    - Área de Qualidade (Testes, QA, automação de testes, etc.)
    
    Você terá 15 perguntas para responder, e cada pergunta terá 5 opções de resposta.
    As opções vão de 1 a 5, onde:
    1 - Discordo totalmente
    2 - Discordo
    3 - Neutro
    4 - Concordo
    5 - Concordo totalmente
    """)
    input(Fore.YELLOW + "Pressione ENTER para continuar...")
    print("O jogo vai começar em 3 segundos...")
    time.sleep(1)
    print("O jogo vai começar em 2 segundos..")
    time.sleep(1)
    print("O jogo vai começar em 1 segundo.")
    time.sleep(1)
    print(Fore.CYAN + "Responda as perguntas abaixo:")
    time.sleep(1)
    p1s = inputValidator("Gosto de programar e resolver problemas com código? ")
    p2s = inputValidator("Tenho interesse em criar aplicativos e sites? ")
    p3s = inputValidator("Gosto de aprender novas linguagens de programação? ")
    p4s = inputValidator("Prefiro trabalhar com lógica e estruturação de código? ")
    p5s = inputValidator("Tenho paciência para depurar erros e otimizar código? ")
    print(Fore.CYAN + "Agora, vamos para a próxima parte!")
    time.sleep(1)
    p6p = inputValidator("Gosto de pensar na experiência do usuário ao usar um sistema? ")
    p7p = inputValidator("Tenho interesse em pesquisa de mercado e comportamento do usuário? ")
    p8p = inputValidator("Me interesso por criar soluções inovadoras e intuitivas? ")
    p9p = inputValidator("Gosto de trabalhar com design, wireframes ou prototipagem? ")
    p10p = inputValidator("Quero entender e definir estratégias para melhorar produtos digitais? ")
    print(Fore.CYAN + "Estou quase lá, só mais algumas perguntas!")
    time.sleep(1)
    p11q = inputValidator("Gosto de testar e garantir que sistemas funcionem corretamente? ")
    p12q = inputValidator("Tenho interesse em encontrar erros e melhorar a estabilidade dos produtos? ")
    p13q = inputValidator("Acredito que testes automatizados ajudam a evitar falhas em sistemas? ")
    p14q = inputValidator("Gosto de seguir padrões e documentar processos para garantir qualidade? ")
    p15q = inputValidator("Quero trabalhar garantindo que um software funcione bem para todos os usuários? ")
    # a soma acontece aqui
    soma1 = p1s + p2s + p3s + p4s + p5s
    soma2 = p6p + p7p + p8p + p9p + p10p
    soma3 = p11q + p12q + p13q + p14q + p15q
    # usei o max pra ver qual é a maior soma e coloquei em uma variável
    betterValue = max(soma1, soma2, soma3)
    # criei uma lista vazia pra colocar as áreas que o usuário se encaixa
    areas = []

    # aqui eu verifico qual das somas é maior e adiciono a área na lista
    if soma1 == betterValue:
        areas.append("dev")
    if soma2 == betterValue:
        areas.append("design")
    if soma3 == betterValue:
        areas.append("qa")

    # pura balaca de novo pra fingir que ta carregando
    print(Fore.CYAN + "Estou pensando, aguarde um momento...")
    time.sleep(3)
    print(Fore.CYAN + "Analisando suas respostas...")
    time.sleep(2)
    print(Fore.CYAN + "Você combina mais com...")
    time.sleep(2)
    print(Fore.LIGHTCYAN_EX + "-------------------------------------------------")
    
    # aqui eu verifico se a lista tem apenas uma área ou mais de uma
    if len(areas) == 1:
        if "dev" in areas: 
            print(Fore.CYAN + "Desenvolvimento de Software")
            print(Fore.LIGHTCYAN_EX + "-------------------------------------------------")
            print("""
            Você pode trabalhar como:
            - Desenvolvedor(a) de Software"
            - Engenheiro(a) de Software"
            - Programador(a) Front-end"
            - Programador(a) Back-end"
            - Cientista de Dados"
            """)
        elif "design" in areas:
            print(Fore.BLUE + "Área de Produtos (UX/UI, Product Owner, Product Manager, etc.")
            print(Fore.LIGHTCYAN_EX + "-------------------------------------------------")
            print("""
            Você pode trabalhar como:
            - Designer de Produtos"
            - UX/UI Designer"
            - Pesquisador(a) de UX"
            - Arquiteto(a) de Informação"
            - Especialista em Experiência do Usuário"
            """)
        else:
            print(Fore.YELLOW + "Área de Qualidade (Testes, QA, automação de testes, etc.)")
            print(Fore.LIGHTCYAN_EX + "-------------------------------------------------")
            print("""
            Você pode trabalhar como:
            - Analista de Testes"
            - Engenheiro(a) de Qualidade"
            - Especialista em Garantia de Qualidade"
            - Testador(a) de Software"
            - Analista de Qualidade de Software"
            """)
    elif len(areas) > 1: # aqui eu verifico se a lista tem mais de uma área
        print(Fore.RED + "Que surpresa! Você pode trabalhar em mais de uma ÁREA das áreas mencionadas.")
        print(Fore.LIGHTCYAN_EX + "-------------------------------------------------")
        time.sleep(1)
        print(Fore.BLUE + "Você pode trabalhar como:")
        if "dev" in areas:
            print("""
            - Desenvolvedor(a) de Software"
            - Engenheiro(a) de Software"
            - Programador(a) Front-end"
            - Programador(a) Back-end"
            - Cientista de Dados"
            """)
        if "design" in areas:
            print("""
            - Designer de Produtos"
            - UX/UI Designer"
            - Pesquisador(a) de UX"
            - Arquiteto(a) de Informação"
            - Especialista em Experiência do Usuário"
            """)
        if "qa" in areas:
            print("""
            - Analista de Testes"
            - Engenheiro(a) de Qualidade"
            - Especialista em Garantia de Qualidade"
            - Testador(a) de Software"
            - Analista de Qualidade de Software"
            """)
    else: # aqui eu verifico se a lista não tem nada, o que não deveria acontecer, mas se acontecer eu reinicio o jogo
        print(Fore.RED + "Opa! Algo deu errado! Vamos reiniciar o jogo.")
        time.sleep(1)
        print("Reiniciando...")
        time.sleep(1)
        return gameInit()
    
    # aqui eu pergunto se o usuário quer jogar de novo
    playAgain = input(Fore.BLUE + "Deseja jogar novamente? (s/n): ")
    if playAgain.lower() == 's':
        print(Fore.YELLOW + "Reiniciando o jogo...")
        time.sleep(1)
        gameInit()
    elif playAgain.lower() == 'n':
        print(Fore.YELLOW + "Obrigado por jogar! Até a próxima!")
        time.sleep(1)
        exit()
    else:
        print(Fore.RED + "Entrada inválida, vamos fechar o jogo.")
        time.sleep(1)
        exit()
        
# aqui eu chamo a função pra iniciar o jogo        
gameInit()