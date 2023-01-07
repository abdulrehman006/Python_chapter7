"""
Modify the Time class of Fig. 7.13 to include a tick method that increments the
time stored in a Time object by one second. The Time object should always remain in a
consistent state. Write a driver program that tests the tick method. Be sure to test the
following cases:
a) Incrementing into the next minute.
b) Incrementing into the next hour.
c) Incrementing into the next day (i.e., 23:59:59 to 0:00:00).
"""


class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.

        hour: int, optional, default: 0
        minute: int, optional, default: 0
        second: int, optional, default: 0
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Returns a string representation of the time."""
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def tick(self):
        """Increments the time by one second."""
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0
			
			
time = Time(23, 59, 59)
print(time)  # 23:59:59
time.tick()
print(time)  # 0:00:00