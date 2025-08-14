#!/usr/bin/env python3

# This file is meant to help work with classes and methods
# The goal of this file is to take input and send back the next or previous second

class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        if len(str(self.hours)) < 2:
            self.hours = '0' + str(self.hours)
        if len(str(self.minutes)) < 2:
            self.minutes = '0' + str(self.minutes)
        if len(str(self.seconds)) < 2:
            self.seconds = '0' + str(self.seconds)
        output = f'{self.hours}:{self.minutes}:{self.seconds}'
        return output

    def next_second(self):
        self.seconds = int(self.seconds)
        self.minutes = int(self.minutes)
        self.hours = int(self.hours)
        if self.seconds < 59:
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes < 59:
                self.minutes += 1
            else:
                self.minutes = 0
                if self.hours < 23:
                    self.hours += 1
                else:
                    self.hours = 0

    def prev_second(self):
        self.seconds = int(self.seconds)
        self.minutes = int(self.minutes)
        self.hours = int(self.hours)
        if self.seconds > 0:
            self.seconds -= 1
        else:
            self.seconds = 59
            if self.minutes > 0:
                self.minutes -= 1
            else:
                self.minutes = 59
                if self.hours > 0:
                    self.hours -= 1
                else:
                    self.hours = 23

if __name__ == "__main__":
    timer = Timer(23, 59, 59)
    print(timer)
    timer.next_second()
    print(timer)
    timer.prev_second()
    print(timer)
