from corpo_humano import CorpoHumano
from deserto import Deserto
from tundra import Tundra
from taiga import Taiga


sair_do_programa = False

while sair_do_programa == False:

    nome = input("Informe seu nome: ")
    corpo = CorpoHumano(nome)

    print("ESCOLHA O BIOMA:")
    print("1 - Deserto")
    print("2 - Tundra")
    print("3 - Taiga")

    opcao = input("Escolha o bioma: ")

    if opcao == "1":
        corpo.periodo = input("Está de dia ou de noite? (dia/noite): ").lower()
        temperatura = float(input("Informe a temperatura atual (°C): "))
        bioma = Deserto(10, temperatura, 30)

    elif opcao == "2":
        temperatura = float(input("Informe a temperatura atual (°C): "))
        bioma = Tundra(60, temperatura, 300, 20)

    elif opcao == "3":
        temperatura = float(input("Informe a temperatura atual (°C): "))
        bioma = Taiga(70, temperatura, -5)

    else:
        print("Opção inválida.")
        exit()
    print()
    bioma.efeito_termico(corpo)

    if opcao == "1":
        print("\nVocê está no deserto, o corpo começa a suar...")
        corpo.suar()


    while True:
        print("MENU:")
        print("1 - Urinar")
        print("2 - Correr")
        print("3 - Sair")
        print("4 - Voltar ao início (novo nome)")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            corpo.urinar()

        elif escolha == "2":
            corpo.correr()

        elif escolha == "3":
            print("Programa encerrado.")
            sair_do_programa = True
            break

        elif escolha == "4":
            print("Voltando ao início...")
            break

        else:
            print("Opção inválida.")
