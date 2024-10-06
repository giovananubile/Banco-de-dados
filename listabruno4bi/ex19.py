
from cryptography.fernet import Fernet
from pymongo import MongoClient


chave = Fernet.generate_key()
fernet = Fernet(chave)


cliente = MongoClient('mongodb+srv://natan:123@cluster0.x640mwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = cliente['lista4']
tabela = db['mensagens']


print("Digite suas mensagens para criptografá-las. Digite 'sair' para encerrar.")


while True:
    mensagem = input("Digite a mensagem: ")
    if mensagem.lower() == 'sair':
        break
    msg_criptografada = fernet.encrypt(mensagem.encode())
    tabela.insert_one({"mensagem_criptografada": msg_criptografada})


print("Todas as mensagens foram criptografadas e armazenadas com sucesso!")

