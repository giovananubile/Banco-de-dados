
from pymongo import MongoClient
from cryptography.fernet import Fernet
from bson.binary import Binary


# A mesma chave Fernet usada para criptografar os dados
chave = b'DgVOMDwzUQH-yVfp1M8XiOBntTG767Xt8Fp-_BpCj78='
fernet = Fernet(chave)


# Conectar ao MongoDB
cliente = MongoClient('mongodb+srv://natan:123@cluster0.x640mwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = cliente['lista4']
tabela = db['dados']


# Procurar a mensagem criptografada no MongoDB
doc = tabela.find_one({"Fernet": {'$exists': True}})
#print(doc)


try:
    if 'Fernet' in doc:
        msg_criptografada = doc['Fernet']  
        msg_descriptografada = fernet.decrypt(msg_criptografada).decode()
        print("Mensagem descriptografada: " + msg_descriptografada)
    else:
        print("Nenhuma mensagem criptografada encontrada no MongoDB.")
except Exception as erro:
    print(f"Erro ao descriptografar: {erro}")

