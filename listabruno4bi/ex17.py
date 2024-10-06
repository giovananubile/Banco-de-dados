
import hashlib


senha = input("Digite a senha para ser criptografada: ")
hash_obj = hashlib.sha256(senha.encode())
hash_senha = hash_obj.hexdigest()
print("Hash da senha em hexadecimal: " + hash_senha)
