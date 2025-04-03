import time
from colorama import init, Fore, Back
init()

def inputValidator(prompt):
    while True:
        try:
            value = int(input(Fore.GREEN + prompt))
            if 1 <= value <= 5:
                return value
            else:
                print("Por favor, insira um número entre 1 e 5. vamos tentar novamente.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número entre 1 e 5.")
            
print(Fore.MAGENTA + "Aguarde, o Jogo está carregando...")
time.sleep(2)
def gamInit():
    print(Fore.GREEN + "Olá! Bem-vindo ao jogo de carreira em tecnologia!")
    print(Fore.YELLOW + "Neste jogo, você responderá a algumas perguntas para descobrir qual área da tecnologia combina mais com você.")
    print(Fore.CYAN + """
    Você terá 15 perguntas para responder, e cada pergunta terá 5 opções de resposta.
    As opções vão de 1 a 5, onde:
    1 - Discordo totalmente
    2 - Discordo
    3 - Neutro
    4 - Concordo
    5 - Concordo totalmente
    """)
    input(Fore.YELLOW + "Pressione qualquer tecla para continuar...")
    print("O jogo vai começar em 3 segundos...")
    time.sleep(1)
    print("2 segundos...")
    time.sleep(1)
    print("1 segundo...")
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

    soma1 = p1s + p2s + p3s + p4s + p5s
    soma2 = p6p + p7p + p8p + p9p + p10p
    soma3 = p11q + p12q + p13q + p14q + p15q
    betterValue = max(soma1, soma2, soma3)
    
    print(Fore.BLACK + Back.WHITE + "Estou pensando, aguarde um momento...")
    time.sleep(3)
    print(Fore.BLACK + Back.WHITE + "Analisando suas respostas...")
    time.sleep(2)
    print(Fore.BLACK + Back.WHITE + "Você combima mais com...")
    time.sleep(2)
    print(Fore.LIGHTCYAN_EX + "-------------------------------------------------")
    if betterValue == soma1:
        print(Fore.CYAN + "Você se saiu melhor na área de programação.")
        print("Você pode trabalhar como:")
        print("- Desenvolvedor(a) de Software")
        print("- Engenheiro(a) de Software")
        print("- Programador(a) Front-end")
        print("- Programador(a) Back-end")
        print("- Cientista de Dados")
    elif betterValue == soma2:
        print(Fore.BLUE + "Você se saiu melhor na área de design de produtos.")
        print("Você pode trabalhar como:")
        print("- Designer de Produtos")
        print("- UX/UI Designer")
        print("- Pesquisador(a) de UX")
        print("- Arquiteto(a) de Informação")
        print("- Especialista em Experiência do Usuário")
    elif betterValue == soma3:
        print(Fore.YELLOW + "Você se saiu melhor na área de qualidade.")
        print("Você pode trabalhar como:")
        print("- Analista de Testes")
        print("- Engenheiro(a) de Qualidade")
        print("- Especialista em Garantia de Qualidade")
        print("- Testador(a) de Software")
        print("- Analista de Qualidade de Software")
    elif betterValue == soma1 and betterValue == soma2 and betterValue == soma3:
        print(Fore.MAGENTA + "Você se saiu igual em todas as áreas.")
        print("Você pode trabalhar como:")
        print("- Desenvolvedor(a) de Software")
        print("- Designer de Produtos")
        print("- Analista de Testes")
    else:
        print(Fore.RED + "Opa! Algo deu errado! Vamos reiniciar o jogo.")
        time.sleep(1)
        print("Reiniciando...")
        time.sleep(1)
        return gamInit()

gamInit()