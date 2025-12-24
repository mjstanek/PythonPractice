import datetime
# Practice code for transforming data structures in Python

# First example:
# Given this dictionary:
# records = [
#     {"user_id": 1, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 1, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 5, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 3, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 4, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 1, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 6, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 1, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 9, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 8, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 7, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 7, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 7, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 8, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 9, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 6, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 6, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 4, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 5, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 6, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 4, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 3, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 3, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 3, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 3, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 3, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 2, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 2, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 1, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 1, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 8, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 7, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 9, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 4, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 5, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 6, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 4, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 2, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 6, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 4, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 3, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 1, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 2, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 5, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 4, "event": "click", "timestamp": "2024-01-01T10:02:00"},
#     {"user_id": 8, "event": "click", "timestamp": "2024-01-01T10:00:00"},
#     {"user_id": 9, "event": "view",  "timestamp": "2024-01-01T10:01:00"},
#     {"user_id": 7, "event": "click", "timestamp": "2024-01-01T10:02:00"},
# ]
# # Transform it into a dictionary of events per user:
# # {
# #   1: {"click": 1, "view": 1},
# #   2: {"click": 1}
# #   etc...
# # }

# def transformRecords(records):
#     sortedRecords = sorted(records, key=lambda item: int(item["user_id"]))
#     # print(sortedRecords)
#     eventDictionary = {}
#     for record in sortedRecords:
#         user = record["user_id"]
#         event = record["event"]
#         # print(f"User {user} did event {event}")
#         if user not in eventDictionary:
#             eventDictionary[user] = {event : 1}
#         else:
#             if event in eventDictionary[user]:
#                 eventCounter = eventDictionary[user][event]
#                 eventCounter += 1
#                 eventDictionary[user][event] = eventCounter
#             else:
#                 eventDictionary[user][event] = 1

#     print(eventDictionary)

# def dedupedRecords(records):
#     mostRecentActivity = {}
#     for record in records:
#         user = record["user_id"]
#         timeStamp = record["timestamp"]
#         if user not in mostRecentActivity:
#             mostRecentActivity[user] = {"event" : record["event"], "timestamp": timeStamp}
#         else:
#             if timeStamp > mostRecentActivity[user]["timestamp"]:
#                 mostRecentActivity[user] = {"event" : record["event"], "timestamp": timeStamp}
#             else:
#                 pass
#     print(mostRecentActivity)


# if __name__ == "__main__":
#     transformRecords(records)
#     dedupedRecords(records)
 
#==============================================================================================
 # Challenge: 
 # Given this array:
events = [
    {"event_id": "e1", "user_id": 1, "event_type": "click", "timestamp": "2024-01-01T10:00:05"},
    {"event_id": "e2", "user_id": 1, "event_type": "view",  "timestamp": "2024-01-01T10:00:10"},
    {"event_id": "e3", "user_id": 2, "event_type": "click", "timestamp": "2024-01-01T10:01:00"},
    {"event_id": "e1", "user_id": 1, "event_type": "click", "timestamp": "2024-01-01T10:00:05"},  # duplicate
    {"event_id": "e4", "user_id": 2, "event_type": "view",  "timestamp": "bad-timestamp"},      # invalid
    {"event_id": "e5", "user_id": None, "event_type": "click", "timestamp": "2024-01-01T10:02:00"}, # invalid
]
# Return a dictionary that has a "User Event Summary" in this shape:
# {
#   user_id: {
#     "total_events": int,
#     "event_counts": {
#         "click": int,
#         "view": int
#     },
#     "first_event_time": str,  # ISO format
#     "last_event_time": str    # ISO format
#   }
# }
# And a metrics in this shape:
# {
#   "total_records": int,
#   "valid_records": int,
#   "invalid_records": int,
#   "duplicate_records": int
# }
# Nest these two dictionaries into one output, with user event by user
# Use this function:

def transformEvents(events):
    eventsOutput = {}
    invalidEvents = 0
    duplicateEvents = 0
    eventNumber = 0
    eventTracker = []
    for event in events:
        eventID = event["event_id"]
        user = event["user_id"]
        timeStamp = event["timestamp"]
        eventType = event["event_type"]
        if (type(user) is int and "bad" not in timeStamp and 
            (eventNumber == 0 or eventID not in eventTracker)):
            if user not in eventsOutput:
                eventsOutput[user] = {"total_events" : 1, "event_counts": {eventType : 1}, 
                                      "first_event_time" : timeStamp, "last_event_time" : timeStamp}
            else:
                newTotalEvents = eventsOutput[user]["total_events"]
                newTotalEvents += 1
                eventsOutput[user]["total_events"] = newTotalEvents
                if eventType in eventsOutput[user]:
                    eventCounter = eventsOutput[user]["event_counts"][eventType]
                    eventCounter += 1
                    eventsOutput[user]["event_counts"][eventType] = eventCounter
                else:
                    eventsOutput[user]["event_counts"][eventType] = 1
                if timeStamp > eventsOutput[user]["last_event_time"]:
                    eventsOutput[user]["last_event_time"] = timeStamp
                elif timeStamp < eventsOutput[user]["first_event_time"]:
                    eventsOutput[user]["first_event_time"] = timeStamp
        else:
            if (type(user) is not int or "bad" in timeStamp):
                invalidEvents +=1
            else:
                duplicateEvents += 1
        eventNumber += 1
        eventTracker.append(eventID)
    metrics = {"total_records" : eventNumber, "valid_records" : (eventNumber - (invalidEvents + duplicateEvents)), 
               "invalid_records" : invalidEvents , "duplicate_records" : duplicateEvents} 
    eventsOutput["metrics"] = metrics   
    print(eventsOutput)             

if __name__ == "__main__":
    transformEvents(events)

# Time = 35 minutes
# Issues:
# 1) Timestamp validation --> I relied too heavily on the phrase "bad-timestamp" 
#       Need to explore more deeply into date/time formatting and parsing
# 2) Timestamp comparisons --> again convert to datetime object
# 3) Missing fully fleshing out the "if eventType in eventsOutput[user]:" line
#       Should be: if eventType in eventsOutput[user]["event_counts"]:
# 4) Final output was incorrectly nested. Should have created new dict and done:
#       finalOutput = "user_event_summary" : eventsOutputs, "metrics" : metrics
# 5) Data Engineering wants eventTracker to be a set, not a list