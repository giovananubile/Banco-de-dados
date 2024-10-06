
from cryptography.fernet import Fernet
from pymongo import MongoClient


chave = Fernet.generate_key()
#print(chave)




cliente = MongoClient('mongodb+srv://natan:123@cluster0.x640mwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = cliente['lista4']
tabela = db['dados']
if tabela.insert_one({'Chave Fernet' : chave}):
    print("chave inserida no banco com sucesso!")
else:
    print("erro ao cadastrar chave!")