"""
------------------------
Create by. Phumin-DEV,
Start Date: 18/02/2022,
Copyright: MIT
Owner: Can be further developed by giving the original copyright.
------------------------
สร้างโดย: Phumin-DEV
วันที่เรื่ม: 18/02/2002
รูปแบบลิชสิทธิ์: MIT
Owner: สามารถพัฒนาต่อยอดได้ โดยให้ลิขสิทธิ์ต้นฉบับไว้ดวย.
------------------------
Follow me on social:
Facebook : https://facebook.com/PhuminMaliwan
Github   : https://github.com/mantvmass
"""

import pip, os, sys, time
from config import printBanner, printBannerc






# check modules import. if not, start installing. / เช็คการนำเข้า module ถ้าไม่มีให้เริ่มการติดตั้ง
try:
    from connect_db import megatronDBC
except ImportError:
    pip.main(['install', '--user', 'mysql-connector-python'])
    from connect_db import megatronDBC

try:
    from pick import pick
except ImportError:
    pip.main(['install', '--user', 'pick'])
    from pick import pick

# end check. / จบการเช็ค


from systems import loginSYS, registerSYS







def home(name, level):
    os.system("cls||clear")
    print(printBannerc(name, level))
    print("\n"
    ,"[1] Chat\n"
    ,"[2] Settings\n"
    ,"[0] Logout")
    try:
        op = int(input("Input choice: "))
        if op > 2:
            print("Alert: Input choice 0 -2 only!")
            time.sleep(3)
            home(name, level)
    except ValueError:
        print("Alert: Input choice 0 -2 only!")
        time.sleep(3)
        home(name, level)
        
    if op == 0:
        os.system("cls||clear")
        print("\nLogout success!")
        sys.exit()
    elif op == 1:
        print("\nChat")
        time.sleep(3)
        home(name, level)
    elif op == 2:
        print("Alert: Input choice 0 -2 only!")
        time.sleep(3)
        home(name, level)


os.system("cls||clear")
while True:
    title = "WELCOME TO MEGATRON"
    options = ['Login', 'Register','Exit']
    # option, index = pick(options, printBanner("",""), indicator='==>')
    option, index = pick(options, title, indicator='==>')
    try:
        if index == 0:          # login
            os.system("cls||clear")
            print(printBanner("",""),"\n")
            print("[ Login ]")
            try:
                userInput = input("USERNAME: ")
                passInput = input("PASSWORD: ")
            except ValueError:
                print("\nValue Error!")
            try:
                check = loginSYS(userInput, passInput)
                if check == 1:
                    os.system("cls||clear")
                    print("\nInvalid username or password!")
                    sys.exit()
                elif check == 2:
                    os.system("cls||clear")
                    print("\nSomething went wrong")
                    sys.exit()
                elif check[0] == 0:
                    print("\nLogin success!")
                    home(check[1],check[2])
                    break
            except:
                sys.exit()  
        elif index == 1:          # register
            os.system("cls||clear")
            print(printBanner("",""),"\n")
            print("[ Register ]")
            try:
                userInput =  input("USERNAME   : ")
                passInput =  input("PASSWORD   : ")
                passInputr = input("RE-PASSWORD: ")
                if passInput != passInputr:
                    print("\nPassword not match!")
                    sys.exit()
            except ValueError:
                print("\nValue Error!")
            try:
                check = registerSYS(userInput, passInput)
                if check == 1:
                    os.system("cls||clear")
                    print("\nUser is already!")
                    sys.exit()
                elif check == 2:
                    os.system("cls||clear")
                    print("\nSomething went wrong")
                    sys.exit()
                elif check == 0:
                    print("\nCreate success!")
                    time.sleep(3)                  
            except:
                sys.exit()  
        elif index == 2:
            os.system("cls||clear")
            print("\nExit success!")
            sys.exit()
    except ValueError:
        print("Something is not right")

