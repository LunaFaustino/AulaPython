usuarios = [
    ["alberto", "1234"],
    ["mario", "6282"],
    ["maria", "5274"],
    ["joana", "9943"]
]

nome = input("Nome de usuário: ")
senha = input("Senha: ")

usuario_encontrado = [nome,senha] in usuarios

if usuario_encontrado:
    msg = f"Acesso liberado"
else:
    msg = "Acesso negado"

print(msg)