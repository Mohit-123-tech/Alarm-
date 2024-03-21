from time import sleep
import playsound
from colorama import Fore

try:
    th = int(input("Enter Alarm in hour : "))
    tm = int(input("Enter Alarm in minutes : "))
except(Exception):
    print(Fore.RED, "Enter Valid Integer Value", Fore.WHITE)
    exit()

sleep(th*3600)
sleep(tm*60)

print(Fore.BLUE, "wake up to realty", Fore.WHITE)
playsound.playsound("Music/m2.mp3")

