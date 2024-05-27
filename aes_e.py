from machine import Pin,UART
from ucryptolib import aes
import ubinascii
import ecc_sender
import html_page
import firebase
#import hillcipher_encrypt

def encrypt(plaintext, key, iv):
    # Padding the plaintext to be a multiple of 16 bytes (AES block size)
    plaintext += b' ' * (16 - (len(plaintext) % 16))

    # Create AES object with key and mode
    cipher = aes(key, 2, iv)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext)

    # Encode the ciphertext using Base64
    ciphertext_base64 = ubinascii.b2a_base64(ciphertext).rstrip().decode('utf-8')

    return ciphertext_base64


ssid=input("Enter the WiFi SSID : ")
password=input("Enter the WiFi Password : ")

data=html_page.main(ssid,password)

#iv_str = input("Enter the IV: ")
iv_str=data[0]
iv = iv_str.encode('utf-8')

# Plain text to be encrypted
#plaintext_str = input("Enter the text: ")

#mac=hillcipher_encrypt.hill_encrypt(plaintext_str)
plaintext = plaintext_str.encode('utf-8')

id=data[1]
recv_id=data[2]

public_key=public_key_retreive.main(ssid,password,data[2])


key=ecc_sender.ecc_secret_key(public_key)

encrypted_text = encrypt(plaintext, key, iv)
encrypted_text = str(len(encrypted_text))+encrypted_text

print("Encrypted text (Base64):", encrypted_text)

firebase.main(ssid,password,id,recv_id,encrypted_text,"0938294a2df95ddfb9568e7266ad02d8bae6ce51f997192cfb80a6b0fa4ab4362f5b0c1b1b8150f3f01e5d3c712f3da6")

#receiver_public_key = "efa262ee09275fa518dec9446526835df7a13b621788382e2403a3ab1d8307423a805609d125f5517b04fcadc98ad4b5"