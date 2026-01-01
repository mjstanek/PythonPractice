# Code to challenge and test my knowledge of the datetime module
# Each Challenge will be delinated

import datetime

# ========== Challenge 1 ==========
# Easy
# Date Validation
# Given the array "events" parse the timestamps and return the number of 
# valid and invalid entries. Correct answer will be 3 valid, 2 invalid

events1 = [
    {"timestamp": "2024-01-01T10:30:00"},
    {"timestamp": "2024-01-01T11:45:00"},
    {"timestamp": "bad-timestamp"},
    {"timestamp": "2024-01-01T12:00:00"},
    {"timestamp": None}
]

def dateValidator(array):
    validDates = 0
    invalidDates = 0
    for event in array:
        try:
            timestamp = datetime.datetime.fromisoformat(event["timestamp"])
            validDates += 1
        # This is where I got dinged - I did not know what the proper errors to catch were
        # I should have used:
        # except (ValueError, TypeError):
        except:
            invalidDates += 1

    outputDictionary = {"valid": validDates, "invalid": invalidDates}
    print(outputDictionary)

if __name__ == "__main__":
    dateValidator(events1)

# ========== Challenge 2 ==========
# Medium
# First and Last event per user
# Given a list of events with a user and timestamp, return the 
# user's first and last event time

events2 = [
    {"user_id": 1, "timestamp": "2024-01-01T09:00:00"},
    {"user_id": 1, "timestamp": "2024-01-01T12:00:00"},
    {"user_id": 2, "timestamp": "2024-01-02T08:30:00"},
    {"user_id": 1, "timestamp": "2024-01-01T10:30:00"},
    {"user_id": 2, "timestamp": "2024-01-02T18:45:00"},
]

# The big takeaway was cleaning the code. I could have looped and done the DateTime stuff
# and input the DateTime formatted data into the outputDictionary array, then, after
# looping through all events, "re-stringified" it:
# Meaning use the timestamp variable in "first_event" and "last_event" then hit it with:
# for user in outputDictionary:
#       outputDictionary[user]["first_event"] = outputDictionary[user]["first_event"].isoformat()
#       outputDictionary[user]["last_event"] = outputDictionary[user]["last_event"].isoformat()

def firstAndLastEvent(array):
    outputDictionary = {}
    for event in array:
        
        timestamp = datetime.datetime.fromisoformat(event["timestamp"])
        
        if event["user_id"] not in outputDictionary:
            
            outputDictionary[event["user_id"]] = {"first_event": event["timestamp"], 
                                                  "last_event": event["timestamp"]}
        else:
            
            firstEvent = datetime.datetime.fromisoformat(outputDictionary[event["user_id"]]["first_event"])
            lastEvent = datetime.datetime.fromisoformat(outputDictionary[event["user_id"]]["last_event"])
            
            if timestamp < firstEvent:
                outputDictionary[event["user_id"]]["first_event"] = event["timestamp"]
            elif timestamp > lastEvent:
                outputDictionary[event["user_id"]]["last_event"] = event["timestamp"]

    print(outputDictionary)

if __name__ == "__main__":
    firstAndLastEvent(events2)

# ========== Challenge 3 ==========
# Hard
# Sessionization
# A session is defined as EITHER the users first event OR an event 30+ minutes 
# after the previous event
# Given an array of events, list the number of sessions per user that

events3 = [
    {"user_id": 1, "timestamp": "2024-01-01T09:00:00"},
    {"user_id": 1, "timestamp": "2024-01-01T09:10:00"},
    {"user_id": 1, "timestamp": "2024-01-01T10:00:00"},  # new session
    {"user_id": 2, "timestamp": "2024-01-01T11:00:00"},
    {"user_id": 2, "timestamp": "2024-01-01T11:20:00"},
    {"user_id": 2, "timestamp": "2024-01-01T12:00:00"},  # new session
]

def sessionCounter(array):
    
    timeDelta = datetime.timedelta(minutes=30)
    outputDictionary = {}
    lastSessionPerUser = {}
    
    for event in array:
        
        timestamp = datetime.datetime.fromisoformat(event["timestamp"])
        user = event["user_id"]

        if user not in outputDictionary:
            outputDictionary[user] = 1
       
        else:
            newSessionTime = lastSessionPerUser[user] + timeDelta
            # I had these in the wrong order, which produced the correct results due to
            # a small sample size. So I incremented the session total per user when
            # an event happened WITHIN 30 minutes instead of over 30 minutes
            if timestamp > newSessionTime:
                outputDictionary[user] += 1
       
        lastSessionPerUser[user] = timestamp

    print(outputDictionary)

if __name__ == "__main__":
    sessionCounter(events3)

# One other thing mentioned was my naming conventions. I have gotten really into camelCase
# thanks to C#, and python seems to be more of a snake_case programming language. I also
# used descriptive names, but not "data engineer-y" names. Apparently they want functions
# named with a verb and then a noun. dateValidator --> count_valid_dates and 
# sessionCounter --> count_user_sessions, but that's minor.
