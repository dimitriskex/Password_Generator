import secrets
import string
import os
from colorama import Fore, Style, init

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    


    characters = ""

    
    if use_upper:
        characters+=string.ascii_uppercase

    if use_lower:
        characters+=string.ascii_lowercase


    if use_digits:
        characters+=string.digits

    if use_special:
        characters+=string.punctuation

    
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":



    os.system("cls" if os.name == "nt" else "clear")  # Clear console

    length=12

    print(Fore.BLUE+ "\t\t Welcome to Code Generator!")


    use_upper=input("📌 Do you want to use upper case letters?(y/n): ").lower()=="y"
    use_lower=input("📌 Do you want to use lower case letters?(y/n): ").lower()=="y"
    use_special=input("📌 Do you want to use punctuations to your password?(y/n): ").lower()=="y"
    use_digits=input("📌 Do you want to use digits?(y/n): " ).lower()== "y"


    password=generate_password(length,use_upper,use_lower,use_digits,use_special)

    print(f"\n🔑 Your password: {password}")

    