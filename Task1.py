import datetime
import time
import winsound

def alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("It's a New Morning!")
            winsound.Beep(1000,2000)
            break
        time.sleep(1)
        

alarm_time = input("Enter your wake up time: ")
alarm(alarm_time)
