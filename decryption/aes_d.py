from ucryptolib import aes
import ubinascii
import ecc_reciever
import html_page
import firebase_receiver
import hillcipher_encrypt

text=''

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

# Key and IV (Initialization Vector)
ssid = input("Enter the WiFi SSID : ")
password = input("Enter the WiFi Password : ")
data=html_page.main(ssid,password)
iv_str=data[0]
recvid=data[1]
iv = iv_str.encode('utf-8')
plaintext_str, key=firebase_receiver.main(ssid,password,recvid)
key=ecc_reciever.ecc_secret_key(key)
a=len(plaintext_str)
l=int(plaintext_str[:2])
iv=plaintext_str[a-16:a]
plaintext_str=plaintext_str[2:l+2]
print(plaintext_str,key,iv)




decrypted_text = decrypt(plaintext_str, key, iv)

text=remove_white_spaces(decrypted_text)



print("Decrypted text:", text)



#sender_public_key : 0938294a2df95ddfb9568e7266ad02d8bae6ce51f997192cfb80a6b0fa4ab4362f5b0c1b1b8150f3f01e5d3c712f3da6   zxfvcv++pp0P0aVFn3u4Vg==