from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import time
from pygame import mixer
import pyfiglet

def reminder(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(5.0)
    mixer.music.play(loops=100)
    while True :
        a = input("Log here: ")
        b = a.upper()
        if b == stopper :
            mixer.music.stop()
            break
        else:
            print("Enter a valid stopper!")

def water_log(msg):
    with open("water_log.txt","a") as f:
        f.write(str(time.asctime(time.localtime(time.time()))) + msg + "\n" )

def eye_log(msg):
    with open("eye_log.txt","a") as f:
        f.write(str(time.asctime(time.localtime(time.time()))) + msg + "\n" )

def phyical_log(msg):
    with open("physical_log.txt", "a") as f:
        f.write(str(time.asctime(time.localtime(time.time()))) + msg + "\n" )


if __name__ == '__main__':

    title = pyfiglet.figlet_format("HEALTH MONITOR", font="digital")
    print(title)
    print("Calculate how much water your body needs in a day : \n")
    a = int(input("Your Weight in Kg : "))
    print(f"Your daily water intake should be",round(a*0.033),"litres")
    print("You should have",round(a*0.033)/0.25,"glass of water in a day. [Note: 1 Glass = 250 ml]")
    print("Along with water, relaxing eyes and doing physical movement is also important, hence this program will remind the same")
    print("\nThe Reminder kicks in as follows : Water = 60 mins : Physical Activity = 60 mins : Eyes = 20 mins" )

    init_water_physical = time.time()
    init_eye = time.time()
    remind_water_physical = 60*60
    remind_eyes = 20*60

    while True:
        if time.time() - init_water_physical > remind_water_physical:
            print("\nTo stop the reminder press [Y] ")
            reminder("Water_physical.mp3","Y")
            init_water_physical = time.time()
            water_log(": Drank Water")
            phyical_log(": Did Physical activity")
            print("Next water and physical activity reminder in 60 mins\n")

        elif time.time() - init_eye > remind_eyes:
            print("\nTo stop the reminder enter [Y] ")
            reminder("eye.mp3","Y")
            init_eye = time.time()
            eye_log(": Eyes Relaxed")
            print("Next Eye reminder in 20 mins\n")



