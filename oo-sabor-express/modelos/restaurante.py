class Restaurante:
    nome = ''
    cotegoria = ''
    ativo = False


restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.nome = 'Bistrô'
restaurante_praca.cotegoria = 'Gourmet'
restaurante_praca.categoria = 'Italiana'
nome_do_restaurante = restaurante_praca.nome
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

restaurantes = [restaurante_praca, restaurante_pizza]
restaurante_pizza.ativo = True
if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')

if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

print(vars(restaurante_praca))
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')