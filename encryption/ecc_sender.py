import os
import tinyec.ec as ec
import tinyec.registry as reg
import binascii

def ecc_secret_key(key):
    # Define the elliptic curve (you may need to adjust this depending on your use case)
    curve = reg.get_curve('secp192r1')
    
    x="d4f45aa92025b041ee6311249e722c107aab657415c62183"
    x=x.encode()
    alice_private_key=binascii.unhexlify(x)
    
    #bob_public_key_derivation
    bob_public_key_hex = key
    bob_public_key_hex_x = bob_public_key_hex[:48]
    bob_public_key_hex_y = bob_public_key_hex[48:]
    bob_public_key_bytes_x = binascii.unhexlify(bob_public_key_hex_x)
    bob_public_key_bytes_y = binascii.unhexlify(bob_public_key_hex_y)
    bob_public_key_x = int.from_bytes(bob_public_key_bytes_x, 'big')
    bob_public_key_y = int.from_bytes(bob_public_key_bytes_y, 'big')
    bob_public_key = ec.Point(curve, bob_public_key_x, bob_public_key_y)
    
    bob_shared_secret = bob_public_key * int.from_bytes(alice_private_key, 'big')
    
    shared_secret_bytes = (bob_shared_secret.x).to_bytes(24, 'big')
    
    shared_key_hex = binascii.hexlify(shared_secret_bytes).decode()
    secret_key=shared_key_hex[:32]
    
    return secret_key


#print(ecc_secret_key("efa262ee09275fa518dec9446526835df7a13b621788382e2403a3ab1d8307423a805609d125f5517b04fcadc98ad4b5"))



#  "secp192r1": {"p": 0xfffffffffffffffffffffffffffffffeffffffffffffffff,
#                "a": 0xfffffffffffffffffffffffffffffffefffffffffffffffc,
#                "b": 0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1,
#                "g": (0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012,
#                      0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811),
#                "n": 0xffffffffffffffffffffffff99def836146bc9b1b4d22831,
#                "h": 0x1}
#bob_public_key = efa262ee09275fa518dec9446526835df7a13b621788382e2403a3ab1d8307423a805609d125f5517b04fcadc98ad4b5


   
    