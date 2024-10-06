
import hashlib
from pymongo import MongoClient


string = input("Digite string para ser validada: ")
hash_obj = hashlib.sha256(string.encode())
hash_obj.hexdigest()
hash_string = hash_obj.hexdigest()


cliente = MongoClient('mongodb+srv://natan:123@cluster0.x640mwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = cliente['lista4']
tabela = db['dados']
if tabela.find_one({'string' : hash_string}):
    print("String validada com sucesso!")
else:
    print("String invalida!")