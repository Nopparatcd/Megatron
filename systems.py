"""
return 0 =  Success
return 1 = Login = 'Invalid username or password!',  Register = 'User is already'
return 2 = 'Something went wrong'
"""

from connect_db import megatronDBC



# login sys / ระบบล็อคอิน
def loginSYS(userInput, passInput):
    try:
        cursor = megatronDBC.cursor()
        selectDB = "SELECT * FROM users;"
        cursor.execute(selectDB)
        result = cursor.fetchall()
        for x in result:
            if userInput == x[1] and passInput == x[2]:
                return 0, x[1], x[3]
        return 1
    except:
        return 2
# end login sys จบระบบล็อคอิน



# register sys / ระบบสมัครสมาชิก
def registerSYS(userInput, passInput):
    try:
        cursor = megatronDBC.cursor()
        selectDB = "SELECT * FROM users;"
        cursor.execute(selectDB)
        result = cursor.fetchall()
        for x in result:
            if userInput == x[1]:
                return 1
        insertDB = f"INSERT INTO users (username, password, level) values ('{userInput}', '{passInput}', 0);"
        cursor.execute(insertDB)
        megatronDBC.commit()
        return 0
    except:
        return 2
# end register sys / จบระบบสมัครสมาชิก

    