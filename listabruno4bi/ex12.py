
from cryptography.fernet import Fernet


with open("lista4b/chave_fernet.txt", "rb") as arquivo_chave:
    chave = arquivo_chave.read()


fernet = Fernet(chave)
mensagem = input("Digite a mensagem para ser criptografada com Fernet: ")
msg_criptografada = fernet.encrypt(mensagem.encode())
print("Mensagem criptografada: ", msg_criptografada.decode())

