personagens = []
for n in range(3):
    nome = input()
    ataque = int(input())
    defesa = int(input())
    personagens.append([nome, (ataque, defesa)])
print(personagens)

maior_ataque = personagens[0][1][0]
nome_maior_ataque = personagens[0][0]
for p in personagens:
    nome = p[0]
    ataque = p[1][0]
    if ataque > maior_ataque:
        maior_ataque = ataque
        nome_maior_ataque = nome

maior_defesa = personagens[0][1][1]
nome_maior_defesa = personagens[0][0]

for p in personagens:
    nome = p[0]
    defesa = p[1][1]
    if defesa > maior_defesa:
        maior_defesa = defesa
        nome_maior_defesa = nome
print("Ataque", nome_maior_ataque, maior_ataque)
print("Defesa", nome_maior_defesa, maior_defesa)
