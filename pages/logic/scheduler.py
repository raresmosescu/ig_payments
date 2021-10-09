from datetime import datetime, date, time

# handles scheduled times
class TimeBlock():
    def __init__(self, date:date) -> None:
        self.scheduled_times = []
        self.date = date

    def add(self, time:time):
        self.scheduled_times.append(time)
        self.sort()
        
    def add_many(self, times:list):
        self.scheduled_times += times
        self.sort()

    def sort(self):
        self.scheduled_times = sorted(self.scheduled_times)

    def remove(self, time:time):
        self.scheduled_times.remove(time)

# handles scheduled dates
class Calendar():
    def __init__(self) -> None:
        self.scheduled_dates = []

    def add(self, date:date):
        self.scheduled_dates.append(date)
        self.sort()
        
    def add_many(self, dates:list):
        self.scheduled_dates += dates
        self.sort()

    def sort(self):
        self.scheduled_dates = sorted(self.scheduled_dates)

    def remove(self, date:date):
        self.scheduled_dates.remove(date)

# handles rules which tell the generator how to generate the available dates list
class GeneratorRule():
    def __init__(self, posts_per_day:int = 0, day_offset:int = 0) -> None:
        self.day_offset = day_offset
        self.posts_per_day = posts_per_day

rule = GeneratorRule(posts_per_day=2, day_offset=1)

cal = Calendar()
cal.add_many([date(2021, 10, 15), date(2021, 10, 12), date(2021, 10, 16)])

print(cal.scheduled_dates)

print(rule.__dict__)
