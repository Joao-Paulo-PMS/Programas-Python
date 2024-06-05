from modelos.restaurante2 import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avalicao('Gui', 10)
restaurante_praca.receber_avalicao("Lais", 8)
restaurante_praca.receber_avalicao("Emy", 5)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()