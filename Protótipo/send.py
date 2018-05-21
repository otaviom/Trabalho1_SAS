def calculateMD5(msg):
    import hashlib
    md5 = hashlib.md5()
    md5.update(msg.encode())
    return md5.hexdigest()

def cript_RSA(object):
    from Crypto import random
    from Crypto.PublicKey import RSA

    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator) #generate public and private keys

    publickey = key.publickey # pub key export for exchange

    print (publickey)


cript_RSA("ola")
