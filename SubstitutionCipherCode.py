def CSCM(key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cm = {}
    for i, char in enumerate(alphabet):
        cm[char] = key[i % len(key)]
    return cm
def encrypt_message(plaintext, key):
    sm = CSCM(key)
    secMessage = ''.join(sm.get(char, char) for char in plaintext.upper())
    return secMessage
def decrypt_message(ciphertext, key):
    sm = CSCM(key)
    decMessage = ''.join(list(sm.keys())[list(sm.values()).index(char)] if char in sm.values() else char for char in ciphertext.upper())
    return decMessage
sharedKey = 'SECRETKEY'
OGmessage = "HELLO"
secretMessage = encrypt_message(OGmessage, sharedKey)
print("If you wanted to encrypt the message:", secretMessage)
decMessage = decrypt_message(secretMessage, sharedKey)
print("If you wanted to decrypt the message:", decMessage)