import time
from datetime import datetime

def alarm_clock():

    print("Simple Alarm Clock")
    alarm_time_str = input("Enter alarm time in HH:MM format (24-hour): ")
    
    print(f"Alarm set for {alarm_time_str}...")

    while True:

        current_time_str = datetime.now().strftime("%H:%M")

        if current_time_str == alarm_time_str:
            print("\nWAKE UP! Alarm ringing!")
            break
        time.sleep(30)

alarm_clock()