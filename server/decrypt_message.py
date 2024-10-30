from cryptography.hazmat.primitives.ciphers.aead import AESGCM


# decifrando uma mensagem usando AES-GCM com IV derivado
def decifrar_mensagem(chave_sessao, iv, mensagem_cifrada):
    aesgcm = AESGCM(chave_sessao)
    mensagem_decifrada = aesgcm.decrypt(iv, mensagem_cifrada, None)
    return mensagem_decifrada