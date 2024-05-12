import adivinhacao
import forca

def escolhe_jogo():
    print("********************************")
    print("Escolha o jogo")
    print("********************************")
    print(" (1) Adivinhação (2) Forca")


    jogo = int(input("Qual jogo vai jogar?"))

    if(jogo == 1):
        print("jogando adivinhacao")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("jogando forca")
        forca.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
