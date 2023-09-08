from connect_bard_service import *
import os

os.system("cls")

while True:
    message = input("Mesaj: ")
    content = chatSairus(message)
    print(f"Sairus: {content}")