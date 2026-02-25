try:
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
except:
    pass

import pygame
import time
import datetime


def set_alarm(alarm_time):
    running = True
    print(f"Alarm set for {alarm_time}")
    sound = "D:\\Coding\\PYTHON\\Exercisses\\AlarmClock\\Alarm.mp3"

    while running:
        current = datetime.datetime.now()
        current = current.strftime("%H:%M:%S")
        print(f"It's {current}", end="\r")

        if current == alarm_time:
            print()
            print("WAKE UP!")

            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            running = False
        time.sleep(1)


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
