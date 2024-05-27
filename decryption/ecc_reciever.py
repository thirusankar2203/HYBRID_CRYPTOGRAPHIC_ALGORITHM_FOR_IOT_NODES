import os
import tinyec.ec as ec
import tinyec.registry as reg
import binascii

def ecc_secret_key(key):
    # Define the elliptic curve (you may need to adjust this depending on your use case)
    curve = reg.get_curve('secp192r1')
    
    x="b32f88575268c4f5bed83cf6ed473b16a6fe24c30d493b1e"
    #Receiver private key
    x=x.encode()
    bob_private_key=binascii.unhexlify(x)
    
    #alice_public_key = 0938294a2df95ddfb9568e7266ad02d8bae6ce51f997192cfb80a6b0fa4ab4362f5b0c1b1b8150f3f01e5d3c712f3da6
    #Sender public key
    #alice_public_key_derivation
    
    alice_public_key_hex = key
    alice_public_key_hex_x = alice_public_key_hex[:48]
    alice_public_key_hex_y = alice_public_key_hex[48:]
    alice_public_key_bytes_x = binascii.unhexlify(alice_public_key_hex_x)
    alice_public_key_bytes_y = binascii.unhexlify(alice_public_key_hex_y)
    alice_public_key_x = int.from_bytes(alice_public_key_bytes_x, 'big')
    alice_public_key_y = int.from_bytes(alice_public_key_bytes_y, 'big')
    
    alice_public_key = ec.Point(curve, alice_public_key_x, alice_public_key_y)
    
    alice_shared_secret = alice_public_key * int.from_bytes(bob_private_key, 'big')
    
    shared_secret_bytes = (alice_shared_secret.x).to_bytes(24, 'big')
    
    shared_key_hex = binascii.hexlify(shared_secret_bytes).decode()
    secret_key=shared_key_hex[:32]
    
    return secret_key


#print(ecc_secret_key("0938294a2df95ddfb9568e7266ad02d8bae6ce51f997192cfb80a6b0fa4ab4362f5b0c1b1b8150f3f01e5d3c712f3da6"))


