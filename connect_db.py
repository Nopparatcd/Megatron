from config import *
import mysql.connector




megatronDBC = mysql.connector.connect(
    host = hostc,
    user = userc,
    password = passc,
    database = dbc
)



