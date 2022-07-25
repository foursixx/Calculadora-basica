import os
from time import sleep

os.system("cls")
print("[!] CARREGANDO DB....")
sleep(1)
os.system("cls")


os.system("color 4")
print('''

################################################
#                                              #
#                                              #
#                                              #
#               CALCULADORA V2                 #
#                                              #
#                                              #
################################################


made by foursix
''')
print('-'*30)


print("[1] SUBTRAÇÃO")
print("[2] MULTIPLICAÇÃO")
print("[3] ADIÇÃO!")
print('-'*30)

try:
    opc = int(input("[+] ESCOLHA OPÇÃO: "))
    if opc == 1: 
        os.system("color 8")
        print("[!] VOCÊ ESCOLHEU SUBTRAÇÃO...")
        sleep(1)
        os.system("cls")
        num1 = int(float(input("[+] PRIMEIRO NUMERO: ")))
        num2 = int(float(input("[+] SEGUNDO NUMERO: ")))
        total1 = num1 - num2
        print('-'*30)
        print(f"[!] O VALOR DEU: {total1}") 
        sair = str(input("[!] DESEJA SAIR? "))
        if sair == "Sim":
            print("[!] SAINDO....")
            sleep(1)
            exit()
        elif sair == "Não":
            print("[!] RETORNANDO PARA A PAGINA INICIAL!")
            sleep(1)
            os.system("cls")
            os.system("python api.py")



    ############################################################
    elif opc == 2:
        os.system("color 1")
        print("[!] VOCÊ ESCOLHEU MULTIPLICAÇÃO...")
        sleep(1)
        os.system("cls")
        num1 = int(float(input("[+] PRIMEIRO NUMERO: ")))
        num2 = int(float(input("[+] SEGUNDO NUMERO: ")))
        total1 = num1 * num2
        print('-'*30)
        print(f"[!] O VALOR DEU: {total1}") 
        sair = str(input("[!] DESEJA SAIR? "))
        if sair == "Sim":
            print("[!] SAINDO....")
            sleep(1)
            exit()
        elif sair == "Não":
            print("[!] RETORNANDO PARA A PAGINA INICIAL!")
            sleep(1)
            os.system("cls")
            os.system("python api.py")




    ############################################################
    elif opc == 3:
        os.system("color 2")
        print("[!] VOCÊ ESCOLHEU ADIÇÃO...")
        sleep(1)
        os.system("cls")
        num1 = int(float(input("[+] PRIMEIRO NUMERO: ")))
        num2 = int(float(input("[+] SEGUNDO NUMERO: ")))
        total1 = num1 + num2
        print('-'*30)
        print(f"[!] O VALOR DEU: {total1}") 
        sair = str(input("[!] DESEJA SAIR? "))
        if sair == "Sim":
            print("[!] SAINDO....")
            sleep(1)
            exit()
        elif sair == "Não":
            print("[!] RETORNANDO PARA A PAGINA INICIAL!")
            sleep(1)
            os.system("cls")
            os.system("python api.py")
except ValueError:
    print("[-] INFORMAÇÃO NÃO DETECTADA NA DB!")
