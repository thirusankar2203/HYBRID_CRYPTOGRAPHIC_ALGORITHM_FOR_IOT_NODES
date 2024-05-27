from machine import Pin,UART,SoftI2C
import time
import dht
from ucryptolib import aes
import ubinascii
import ecc_sender
import html_page
import firebase
import twilio
import public_key_retreive
import ssd1306
import urandom

i2c = SoftI2C(scl=Pin(22),sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128,64,i2c)

dhtdata = dht.DHT11(Pin(15))

def generate_iv():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    iv=''
    iv = iv.join(urandom.choice(characters) for x in range(16))
    return iv

def encrypt(plaintext, key, iv):
    # Create AES object with key and mode
    plaintext += b' ' * (16 - (len(plaintext) % 16))
    cipher = aes(key, 2, iv)

    # Encrypt the plaintext
    encrypted_text = cipher.encrypt(plaintext)

    # Encode the ciphertext using Base64
    ciphertext_base64 = ubinascii.b2a_base64(encrypted_text).rstrip().decode('utf-8')

    return ciphertext_base64

def main():
    ssid="LAPTOP"#"ACTFIBERNET"#input("Enter the WiFi SSID : ")
    password="12345678"#"act12345"#input("Enter the WiFi Password : ")
    #twilio.connect_wifi(ssid, password)

    data=html_page.main(ssid,password)

    iv_str=generate_iv()
    id=data[0]
    recv_id=data[1]
    print(recv_id)
    public_key=public_key_retreive.main(ssid,password,recv_id)
    print(public_key)
    iv = iv_str.encode('utf-8')

    while True:
        dhtdata.measure()
        oled.fill(0)
        oled.show()
        oled.text("Temperature : "+str(dhtdata.temperature()),0,10)
        oled.show()
        oled.text("Humidity : "+str(dhtdata.humidity()),0,30)
        oled.show()
        plaintext_str = "Temperature" + str(dhtdata.temperature()) + "&Humidity" + str(dhtdata.humidity())
        print(plaintext_str)
        plaintext = plaintext_str.encode('utf-8')
        print(plaintext)

        key=ecc_sender.ecc_secret_key(public_key)
        print(key)

        encrypted_text = encrypt(plaintext, key, iv)
        print(encrypted_text)
        encrypted_text = str(len(encrypted_text))+encrypted_text+iv_str

        print("Encrypted text (Base64):", encrypted_text)

        firebase.main(ssid,password,id,recv_id,encrypted_text,"0938294a2df95ddfb9568e7266ad02d8bae6ce51f997192cfb80a6b0fa4ab4362f5b0c1b1b8150f3f01e5d3c712f3da6")
        time.sleep(10)
#receiver_public_key = "efa262ee09275fa518dec9446526835df7a13b621788382e2403a3ab1d8307423a805609d125f5517b04fcadc98ad4b5"

main()