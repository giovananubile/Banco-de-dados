
import hashlib
from pymongo import MongoClient


def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


cliente = MongoClient('mongodb+srv://natan:123@cluster0.x640mwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = cliente['lista4']
tabela = db['usuarios']


senha = input("Digite a senha para ser armazenada: ")
hash_senha = gerar_hash(senha)


tabela.insert_one({"hash_senha": hash_senha})
print("Senha armazenada com sucesso!")


senha_validacao = input("Digite a senha para validar: ")
hash_validacao = gerar_hash(senha_validacao)


usuario = tabela.find_one({"hash_senha": hash_senha})


if usuario:
    if hash_validacao == hash_senha:
        print("Senha válida!")
    else:
        print("Senha inválida!")
else:
    print("Senha não encontrada!")

