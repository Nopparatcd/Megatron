# setting db connection / ตั้งค่าการเชื่อมต่อ db
from ast import Global


hostc = "127.0.0.1"
userc = "root"
passc = ""
dbc = "megatron"





# setting banner / ตั้งค่า banner  1
def printBanner(name_user, level):
    # check name
    if name_user != "":
        show_name = f"Connect: {name_user}"
    else:
        show_name = ""
    # set rank
    if str(level) == "0":
        show_rank = "Rank   : User"
    elif str(level) == "1":
        show_rank = "Rank   : Admin"
    elif str(level) == "2":
        show_rank = "Rank   : Owner"
    else:
        show_rank = ""
    banner = f"""
███╗   ███╗████████╗ [ MEGATRON V.Demo ]
████╗ ████║╚══██╔══╝
██╔████╔██║   ██║    {show_name}
██║╚██╔╝██║   ██║    {show_rank}
██║ ╚═╝ ██║   ██║   
╚═╝     ╚═╝   ╚═╝    Create By.Phumin-DEV"""
    return banner

# setting banner / ตั้งค่า banner  2
def printBannerc(name_user, level):
    # check name
    if name_user != "":
        show_name = f"\033[0;37;42m Connect\033[0;37;40m: {name_user}"
    else:
        show_name = ""
    # set rank
    if str(level) == "0":
        show_rank = "\033[0;30;44m Rank   \033[0;37;40m: User"
    elif str(level) == "1":
        show_rank = "\033[0;30;44m Rank   \033[0;37;40m: Admin"
    elif str(level) == "2":
        show_rank = "\033[0;37;45m Rank   \033[0;37;40m: Owner"
    else:
        show_rank = ""
    banner = f"""
\033[5;34;40m███╗   ███╗████████╗\033[0;37;40m [ MEGATRON V.Demo ]
\033[5;34;40m████╗ ████║╚══██╔══╝\033[0;37;40m
\033[5;34;40m██╔████╔██║   ██║   \033[0;37;40m {show_name}
\033[5;34;40m██║╚██╔╝██║   ██║   \033[0;37;40m {show_rank}
\033[5;34;40m██║ ╚═╝ ██║   ██║   \033[0;37;40m
\033[5;34;40m╚═╝     ╚═╝   ╚═╝   \033[0;37;40m Create By.Phumin-DEV"""
    return banner

# print(printBanner("",""))