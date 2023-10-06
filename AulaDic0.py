meu_dict = dict()
meudict = { }
meudict["nome"] = "Luna"
meudict["idade"] = 23
meudict["sexo"] = "feminino"

print(meudict)

meudict["sexo"] = "masculino"

print(meudict)

meudict["sobrenome"] = 'Faustino'

print(meudict)

del meudict["sexo"]

print(meudict)

print(len(meudict))

print(meudict.values())

for chave in meudict.keys():
    print(chave)

for valor in meudict.values():
    print(valor)

for var in meudict.items():
    print(var)

print("###################################")

for chave, valor in meudict.items():
    print(chave, valor)

for chave, valor in meudict.items():
    print(f"A chave é: {chave} e o valor é {valor}")

    