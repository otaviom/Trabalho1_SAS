def calculateMD5(msg):
    import hashlib
    md5 = hashlib.md5()
    md5.update(msg.encode())
    encrypt(md5.hexdigest(),type='hash')

def generate_keys():
    from Crypto.PublicKey import RSA

    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open("privatek.pem", "wb")
    file_out.write(private_key)

    public_key = key.publickey().export_key()
    file_out = open("publick.pem", "wb")
    file_out.write(public_key)
    print ('Chaves geradas!')

def encrypt(data, type='message'):
    from Crypto.PublicKey import RSA
    from Crypto.Random import get_random_bytes
    from Crypto.Cipher import AES, PKCS1_OAEP

    data = data.encode("utf-8")
    if type == 'message':
        file_out = open("arquivos\encrypted_message.bin", "wb")
    else:
        file_out = open("arquivos\encrypted_hash.bin", "wb")

    recipient_key = RSA.import_key(open("publicK.pem").read())
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]

#-------------------------------------------------------------------------------#
def generate_message():
    message = input("Digite a mensagem a ser enviada: ")

    calculateMD5(message)
    encrypt(message)

    print ('Mensagem devidamente criptografada e pronta para ser enviada.')
