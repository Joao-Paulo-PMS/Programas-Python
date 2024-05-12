import random
def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")


    numero_secreto =random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de difculdade:")
    print(" (1)facil (2) medio (3) dificil")

    nivel = int(input("qual o nivel?"))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
    for rodada in range(1,total_de_tentativas +1):
        print("Tentativas {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100:")

        print("Voce digitou:", chute_str)
        chute   = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100:")
            continue

        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Voce acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Voce errou! seu chute foi maior que o numero secreto.")
            elif (menor):
                print("Voce errou! seu chute foi menor que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (rodada == total_de_tentativas):
                print("O número secreto era {}. Você fez {}".format(
                    numero_secreto, pontos))
        print("Fim do jogo")
if(__name__ == "__main__"):
    jogar()