
import hashlib


senha = input("Digite senha para ser criptografada: ")


#SHA-256
hash = hashlib.sha256(senha.encode())
hash_SHA256 = hash.hexdigest()
tamanho_hash_SHA256 = len(hash_SHA256)
print(f"Tamanho do Hash SHA-256 da senha: {tamanho_hash_SHA256}")


#MD5
hash = hashlib.md5(senha.encode())
hash_MD5 = hash.hexdigest()
print(f"Tamanho do Hash MD5 da senha: {len(hash_MD5)}")


#MD5
hash = hashlib.sha1(senha.encode())
hash_SHA1 = hash.hexdigest()
print(f"Tamanho do Hash SHA1 da senha: {len(hash_SHA1)}")