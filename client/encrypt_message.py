from cryptography.hazmat.primitives.ciphers.aead import AESGCM


# cifrando uma mensagem usando AES-GCM
def cifrar_mensagem(chave_sessao, mensagem, iv):
    aesgcm = AESGCM(chave_sessao)
    mensagem_cifrada = aesgcm.encrypt(iv, mensagem, None)
    return mensagem_cifrada
