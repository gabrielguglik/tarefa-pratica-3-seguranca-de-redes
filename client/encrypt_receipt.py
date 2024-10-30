import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


# cifrando o comprovante usando AES-GCM
def cifrar_comprovante(chave_sessao, comprovante, iv):
    aesgcm = AESGCM(chave_sessao)
    comprovante_cifrado = aesgcm.encrypt(iv, comprovante, None)
    return comprovante_cifrado

