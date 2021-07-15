# AES-CBC-POLY_1305
import secrets
import scrypt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import Poly1305
import hashlib


class Symmetric_Cryptography:

    def __init__(self):
        self.authentication = 0

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
        return cipher_text + iv

    @staticmethod
    def symmetric_decryption(cipher_txt, key):
        iv = cipher_txt[len(cipher_txt) - 16:]
        cipher_text = cipher_txt[: len(cipher_txt) - 16]
        aes_dec = AES.new(key, AES.MODE_CBC, iv)
        message = unpad(aes_dec.decrypt(cipher_text), AES.block_size)
        msg = message.decode('utf-8')
        return msg

    @staticmethod
    def generate_Poly1305_mac(data, key):
        mac = Poly1305.new(key=key, cipher=AES, data=data)
        return mac.hexdigest(), mac.nonce

    def verify_Poly1305_mac(self, data, key, nonce, mac_digest):
        mac_verify = Poly1305.new(data=data, key=key, nonce=nonce,
                                  cipher=AES)
        try:
            mac_verify.hexverify(mac_digest)
            self.authentication = 1
        except:
            self.authentication = 0
        return self.authentication

    @staticmethod
    def my_hash(key):
        hashed = hashlib.new('sha256')
        hashed.update(key)
        digest_key = hashed.digest()
        return digest_key

