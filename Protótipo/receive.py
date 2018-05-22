def calculateMD5(msg):
    import hashlib
    md5 = hashlib.md5()
    md5.update(msg.encode())
    return md5.hexdigest()

def decrypt(type='message'):
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import AES, PKCS1_OAEP

    if type == 'message':
        file_in = open("arquivos\encrypted_message.bin", "rb")
    else:
        file_in = open("arquivos\encrypted_hash.bin", "rb")

    private_key = RSA.import_key(open("privateK.pem").read())

    enc_session_key, nonce, tag, ciphertext = \
   [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

    # Decrypt the session key with the private RSA key
    cipher_rsa = PKCS1_OAEP.new(private_key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)

    return data.decode("utf-8")

def confirm_hash(msg):
    if calculateMD5(msg) == decrypt(type='hash'):
        return True
    else:
        return False

#------------------------------------------------------------------------------#

message = decrypt()
if confirm_hash(message):
    print ('Mensagem não comprometida: "' + message + '"')
else:
    print ('Mensagem comprometida: "' + message + '"')
