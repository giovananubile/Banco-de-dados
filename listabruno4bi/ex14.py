
from pymongo import MongoClient
from cryptography.fernet import Fernet
conexao = MongoClient('mongodb+srv://natan:123@cluster0.x640mwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
banco = conexao['lista4']
tabela = banco['dados']


doc = tabela.find_one({'Chave Fernet' : {'$exists': True}})
if doc:
    chave = doc['Chave Fernet']
    fernet = Fernet(chave)


    msg = input("digite mensagem: ")
    msg_criptografada = fernet.encrypt(msg.encode())
   
    msg_descriptografada = fernet.decrypt(msg_criptografada.decode())
    print("Mensagem decodificada: " + msg_descriptografada.decode())