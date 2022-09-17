import sqlite3

import bcrypt
print('Login!')
print
user_password = input("Passsword: ")
password_sale = bcrypt.gensalt()
hashed_pw = bcrypt.hashpw(user_password.encode(),password_sale)
print(hashed_pw)
decoded_pw = hashed_pw.decode()
print(decoded_pw)
check_pass = bcrypt.checkpw(user_password.encode(),decoded_pw.encode())