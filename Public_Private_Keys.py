from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify
from os import chmod

#Generating private key (RsaKey object) of key length of 1024 bits
private_key = RSA.generate(2048)

#Generating the public key (RsaKey object) from the private key
public_key = private_key.publickey()
print(type(private_key), type(public_key))

#Converting the RsaKey objects to string 
private_pem = private_key.export_key().decode()
public_pem = public_key.export_key().decode()
print(type(private_pem), type(public_pem))

#Writing down the private and public keys to 'pem' files
with open('keys/server_private.pem', 'w') as pr:
    chmod("keys/server_private.pem", 0o600)
    pr.write(private_pem)
with open('keys/server_public.pem', 'w') as pu:
    pu.write(public_pem)
