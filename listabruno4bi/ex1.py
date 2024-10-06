
import hashlib
senha = input("Digite senha para ser criptografada: ")
hash_obj = hashlib.sha256(senha.encode())
hash_obj.hexdigest()
hash_senha = hash_obj.hexdigest()
print("Hash da senha: "+ hash_senha)