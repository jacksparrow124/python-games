import string
import secrets

symbols = ['*', '%', '£', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', '!', '@', '#', '$'] # Can add more

password = ""
for _ in range(9):
    password += secrets.choice(string.ascii_lowercase)
password += secrets.choice(string.ascii_uppercase)
password += secrets.choice(string.digits)
password += secrets.choice(symbols)
print(password)