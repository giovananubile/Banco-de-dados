
import hashlib


senha = input("Digite senha para ser criptografada: ")
hash_obj = hashlib.md5(senha.encode())
hash_obj.hexdigest()
hash_senha = hash_obj.hexdigest()
print("Hash MD5 da senha: "+ hash_senha)