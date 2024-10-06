
import hashlib


senha = input("Digite senha para ser criptografada: ")


#SHA-256
hash = hashlib.sha256(senha.encode())
hash_SHA256 = hash.hexdigest()
print("Hash SHA-256 da senha: "+ hash_SHA256)


#MD5
hash = hashlib.md5(senha.encode())
hash_MD5 = hash.hexdigest()
print("Hash MD5 da senha: "+ hash_MD5)


#MD5
hash = hashlib.sha1(senha.encode())
hash_SHA1 = hash.hexdigest()
print("Hash MD5 da senha: "+ hash_SHA1)
