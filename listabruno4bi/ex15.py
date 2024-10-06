
from cryptography.fernet import Fernet


with open("lista4b/chave_fernet.txt", "rb") as arquivo_chave:
    chave = arquivo_chave.read()


fernet = Fernet(chave)


caminho_arquivo = input("Digite o caminho do arquivo de texto a ser criptografado: ")


with open(caminho_arquivo, "rb") as arquivo:
    conteudo = arquivo.read()


conteudo_criptografado = fernet.encrypt(conteudo)


caminho_arquivo_criptografado = caminho_arquivo + ".enc"
with open(caminho_arquivo_criptografado, "wb") as arquivo_criptografado:
    arquivo_criptografado.write(conteudo_criptografado)


print(f"Arquivo criptografado e salvo como: {caminho_arquivo_criptografado}")

