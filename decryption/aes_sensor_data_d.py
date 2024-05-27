from ucryptolib import aes
import time
import ubinascii
import ecc_reciever
import html_page
import firebase_receiver
import blynk
import twilio

def remove_white_spaces(decrypted_text):
    text=''
    for i in range(len(decrypted_text)):
        if(decrypted_text[i]!=' '):
            text+=decrypted_text[i]
    return text

def decrypt(ciphertext_base64, key, iv):
    # Decode the ciphertext from Base64
    ciphertext = ubinascii.a2b_base64(ciphertext_base64)

    # Create AES object with key and mode
    decipher = aes(key, 2, iv)

    # Decrypt the ciphertext
    decrypted_text = decipher.decrypt(ciphertext)

    return decrypted_text.decode('utf-8')

def main():
    # Enter the WiFi Credentials
    ssid = "LAPTOP"#"ACTFIBERNET"#input("Enter the WiFi SSID : ")
    password = "12345678"#"act12345"#input("Enter the WiFi Password : ")
    twilio.connect_wifi(ssid, password)
    
    # Send the credentials to the HTML form
    data=html_page.main(ssid,password)

    # Receive data from the HTML form
    recvid=data[0]
    print(recvid)
    while True:
        # Retreive data from the Firebase using the unique receiver ID
        plaintext_str, key, sendid=firebase_receiver.main(ssid,password,recvid)
        
        # Get the secret key from ECC_RECEIVER
        key=ecc_reciever.ecc_secret_key(key)
        
        # Retreive the Plaintext and the Initialization vector from the Firebase data
        a=len(plaintext_str)
        l=int(plaintext_str[:2])
        iv=plaintext_str[a-16:a]
        plaintext_str=plaintext_str[2:l+2]
        print(plaintext_str,key,iv)

        # decrypt the data received using AES decryption
        decrypted_text = decrypt(plaintext_str, key, iv)
        text=remove_white_spaces(decrypted_text)
        list=text.split('&')
        temp = list[0]
        temp = temp[len(temp)-2:len(temp)]
        humi = list[1]
        humi = humi[len(humi)-2:len(humi)]
        print("Temperature : "+temp+" , Humidity : "+humi)
        
        temp = sendid + " : " + str(temp)
        humi = sendid + " : " + str(humi)
        blynk.main(ssid,password,temp,humi)
        
        time.sleep(1)
        
main()

#sender_public_key : 0938294a2df95ddfb9568e7266ad02d8bae6ce51f997192cfb80a6b0fa4ab4362f5b0c1b1b8150f3f01e5d3c712f3da6   zxfvcv++pp0P0aVFn3u4Vg==
