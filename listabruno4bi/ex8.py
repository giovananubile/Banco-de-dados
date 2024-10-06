
from cryptography.fernet import Fernet
# Gerando uma chave secreta
chave = 'DgVOMDwzUQH-yVfp1M8XiOBntTG767Xt8Fp-_BpCj78='
fernet = Fernet(chave)


#criptografando dados
mensagem = input("Digite mensagem para ser criptografada: ")
msg_criptografada = fernet.encrypt(mensagem.encode())
print("Mensagem criptografada com Fernet: " + msg_criptografada.decode())


#descriptografar dados
msg_descriptografada = fernet.decrypt(msg_criptografada).decode()
print("Mensagem descriptografada: " + msg_descriptografada)
