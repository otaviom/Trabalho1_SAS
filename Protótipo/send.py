def calculateMD5(msg):
    import hashlib
    md5 = hashlib.md5()
    md5.update(msg.encode())
    return md5.hexdigest()


msg = input("Digite a mensagem: ")

print(calculateMD5(msg))
