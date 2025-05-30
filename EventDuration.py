#!/usr/bin/env python3

# This practice file demonstrates how to calculate the duration of an event in Python.
# This script will demonstrate the input and print functions.

def event_duration():
    try:
        hour = int(input("What hour will the event start at?: "))


        if hour < 0 or hour > 23:
            print("Invalid hour. Please enter a value between 0 and 23.")
            return
        
        minutes = int(input("What minute will the event start at?: "))
        
        if minutes < 0 or minutes > 59:
            print("Invalid minutes. Please enter a value between 0 and 59.")
            return
        
        duration = int(input("How long, in minutes, will the event last?: "))
        
        if duration > 0:  
            durationhours = int(duration/60)
            duartionminutes = duration % 60
            endhours = hour + durationhours
            endminutes = minutes + duartionminutes

            if endminutes > 59:
                endhours = endhours + (int(endminutes/60))
                endminutes = (endminutes % 60)

            if endhours > 23:
                endhours = endhours % 24

            print(f'This event will end at {endhours}:{endminutes}.')
        else:
            print("Invalid duration. Please enter a positive value for the duration in minutes.")
            return
    
    except ValueError:
        print("Invalid input. Please enter numeric values for hour, minute, and duration.")

if __name__ == "__main__":
    event_duration()
    