import send
import receive

option = input('1. Gerar mensagem criptografada;\n2. Descriptografar mensagem;\n3. Gerar par de chaves;\n4. Apagar mensagens;\nOpção: ')

if option == '3':
    send.generate_keys()
elif option == '1':
    send.generate_message()
elif option == '2':
     receive.read_message()
elif option == '4':
    receive.remove_message()
else:
    print('Opção Inválida')
