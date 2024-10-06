
from cryptography.fernet import Fernet


chave = Fernet.generate_key()
fernet = Fernet(chave)
with open("lista4b/chave_fernet.txt", "wb") as arquivo_chave:
    arquivo_chave.write(chave)


print(f"Chave Fernet gerada e salva no arquivo 'chave_fernet.key': {chave.decode()}")
