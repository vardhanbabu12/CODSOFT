import random
alp_l="abcdefghijklmnopqrstuvwxyz"
alp_h=alp_l.upper()
numbers="1234567890"
symbols="~`@#$%^&*\|+-*/"
password=alp_l+alp_h+numbers+symbols
length_password=int(input("Enter the length of password:"))
a="".join(random.sample(password,length_password))
print(f"Your password is {a}") 
