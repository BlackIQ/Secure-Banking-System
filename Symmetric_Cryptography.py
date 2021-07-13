# AES-CBC-POLY_1305
import secrets
import scrypt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class Symmetric_Cryptography:

    @staticmethod
    def key_generation():
        password = open('password.txt', 'r').read()
        salt = secrets.token_bytes(32)
        key = scrypt.hash(password, salt, N=2048, r=8, p=1, buflen=32)
        return key

    @staticmethod
    def symmetric_encryption(msg, key):
        aes_enc = AES.new(key, AES.MODE_CBC)
        cipher_text = aes_enc.encrypt(pad(msg, AES.block_size))
        iv = aes_enc.iv
        return iv, cipher_text

    @staticmethod
    def symmetric_decryption(cipher_txt, key, iv):
        aes_dec = AES.new(key, AES.MODE_CBC, iv)
        message = unpad(aes_dec.decrypt(cipher_txt), AES.block_size)
        msg = message.decode('utf-8')
        return msg



