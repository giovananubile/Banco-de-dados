
import hashlib


def gerar_hash(arquivo):
    """Gera o hash SHA-256 de um arquivo."""
    hash_obj = hashlib.sha256()
    with open(arquivo, "rb") as f:
        for byte_chunk in iter(lambda: f.read(4096), b""):
            hash_obj.update(byte_chunk)
    return hash_obj.hexdigest()


caminho_arquivo = input("Digite o caminho do arquivo para verificar a integridade: ")


hash_original = gerar_hash(caminho_arquivo)
print("Hash original: " + hash_original)


input("Faça uma alteração no arquivo e pressione Enter para continuar...")


hash_atual = gerar_hash(caminho_arquivo)
print("Hash atual: " + hash_atual)


if hash_original == hash_atual:
    print("O arquivo não foi alterado.")
else:
    print("O arquivo foi alterado.")