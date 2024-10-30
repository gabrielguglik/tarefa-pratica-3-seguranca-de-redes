from cryptography.hazmat.primitives.ciphers.aead import AESGCM


# decifrando o comprovante usando AES-GCM
def decifrar_comprovante(chave_sessao, iv, comprovante_cifrado):
    aesgcm = AESGCM(chave_sessao)
    comprovante_decifrado = aesgcm.decrypt(iv, comprovante_cifrado, None)
    return comprovante_decifrado