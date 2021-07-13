from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash.SHA256 import SHA256Hash
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
import binascii


class Encryption_Decryption:
    @staticmethod
    def encryption_server_public_key(message):
        pu_key = RSA.import_key(open('keys/server_public.pem', 'r').read())
        cipher = PKCS1_OAEP.new(key=pu_key)
        cipher_text = cipher.encrypt(message)
        return cipher_text

    @staticmethod
    def decryption_server_private_key(cipher_text):
        pr_key = RSA.import_key(open('keys/server_private.pem', 'r').read())
        decrypt = PKCS1_OAEP.new(key=pr_key)
        decrypted_message = decrypt.decrypt( cipher_text)
        return decrypted_message

    @staticmethod
    def encryption_client_public_key(message):
        pu_key = RSA.import_key(open('keys/client_public.pem', 'r').read())
        cipher = PKCS1_OAEP.new(key=pu_key)
        cipher_text = cipher.encrypt(message)
        return cipher_text

    @staticmethod
    def decryption_client_private_key(cipher_text):
        pr_key = RSA.import_key(open('keys/client_private.pem', 'r').read())
        decrypt = PKCS1_OAEP.new(key=pr_key)
        decrypted_message = decrypt.decrypt(cipher_text)
        return decrypted_message


class Sign_Verify:
    @staticmethod
    def sign_server_private_key(message):
        pr_key = RSA.import_key(open('keys/server_private.pem', 'r').read())
        digest_msg = SHA256.new(message)
        signer = PKCS1_v1_5.new(pr_key)
        sig = signer.sign(digest_msg)
        return sig, message

    @staticmethod
    def verify_server_public_key(signed_message, message):
        pu_key = RSA.import_key(open('keys/server_public.pem', 'r').read())
        verifier = PKCS1_v1_5.new(pu_key)
        digest_message = SHA256.new(message)
        verification = 0
        try:
            verifier.verify(digest_message, signed_message)
            print("Signature is valid.")
            verification = 1
        except:
            print("Signature is invalid.")
            verification = 0
        return verification

    # for client

    @staticmethod
    def sign_client_private_key(message):
        pr_key = RSA.import_key(open('keys/client_private.pem', 'r').read())
        digest_msg = SHA256.new(message)
        signer = PKCS1_v1_5.new(pr_key)
        sig = signer.sign(digest_msg)
        return sig, message

    @staticmethod
    def verify_client_public_key(signed_message, message):
        pu_key = RSA.import_key(open('keys/client_public.pem', 'r').read())
        verifier = PKCS1_v1_5.new(pu_key)
        digest_message = SHA256.new(message)
        verification = 0
        try:
            verifier.verify(digest_message, signed_message)
            print("Signature is valid.")
            verification = 1
        except:
            print("Signature is invalid.")
            verification = 0
        return verification
