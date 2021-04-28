# random generate 
# import string	
# user_name = input("enter your name")
# print(user_name[::-1])
# x = string.punctuation 
# print(user_name + x)

import secrets	
user_name = input("enter your name")
print(user_name[::-1])
x = secrets.token_hex()
print(user_name + x)

