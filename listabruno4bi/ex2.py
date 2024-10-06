import hashlib


string = input("Digite string para ser criptografada: ")
string2 = input("Digite string2 para ser criptografada: ")
hash_obj = hashlib.sha256(string.encode())
hash_obj2 = hashlib.sha256(string2.encode())
hash_obj.hexdigest()
hash_obj2.hexdigest()
hash_string = hash_obj.hexdigest()
hash_string2 = hash_obj2.hexdigest()
#print("Hash da string: "+ hash_string)
#print("Hash da string2: "+ hash_string2)


if hash_string == hash_string2:
    print("Hash compativel!")
else:
    print("Hash incompativel!")
