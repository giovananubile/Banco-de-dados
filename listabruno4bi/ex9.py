
from pymongo import MongoClient
from cryptography.fernet import Fernet
# Gerando uma chave secreta
chave = 'DgVOMDwzUQH-yVfp1M8XiOBntTG767Xt8Fp-_BpCj78='
fernet = Fernet(chave)


#criptografando dados
mensagem = input("Digite mensagem para ser criptografada com Fernet: ")
msg_criptografada = fernet.encrypt(mensagem.encode())
print(msg_criptografada)


#descriptografar dados
msg_descriptografada = fernet.decrypt(msg_criptografada).decode()
#print("Mensagem descriptografada: " + msg_descriptografada)


cliente = MongoClient('mongodb+srv://natan:123@cluster0.x640mwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = cliente['lista4']
tabela = db['dados']
if tabela.insert_one({"Fernet" : msg_criptografada}):
    print("inserido com sucesso!")
else:
    print("erro ao inserir!")