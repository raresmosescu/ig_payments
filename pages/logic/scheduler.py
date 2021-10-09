from datetime import datetime, date, time, timedelta

# handles scheduled times
class Day():
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

class SchedulerGenerator():
  def __init__(self, rules: GeneratorRule, calendar: Calendar, posts: int, start_date: date) -> None:
    self.unavailable_dates = []
    self.available_dates = []
    self.rules = rules
    self.calendar = calendar
    self.posts = posts
    self.start_date = start_date
  
  def add_unavailable(self, dates: list):
    for item in dates:
      if item not in self.unavailable_dates:
        self.unavailable_dates.append(item)
    self.sort() 
    
  def sort(self):
    self.unavailable_dates = sorted(self.unavailable_dates)
    
  def get_unavailable_dates(self):
    if self.rules.day_offset > 0:
      for item in self.calendar.scheduled_dates:
        current_offset = self.rules.day_offset
        while current_offset > 0:
          self.add_unavailable([
            item, 
            item + timedelta(days=current_offset), 
            item - timedelta(days=current_offset)
          ])
          current_offset = current_offset - 1
  
  def get_available_dates(self):
    self.get_unavailable_dates()
    current_date = self.start_date
    current_posts = self.posts
    while current_posts > 0:
      if current_date not in self.unavailable_dates:
        print(current_date)
        current_posts = current_posts - self.rules.posts_per_day
      current_date = current_date + timedelta(days=1)


rules = GeneratorRule(posts_per_day=2, day_offset=1)

cal = Calendar()
cal.add_many([date(2021, 10, 12), date(2021, 10, 15), date(2021, 10, 20)])

scheduler = SchedulerGenerator(rules, cal, 15, date.today())

scheduler.get_available_dates()

# print(cal.scheduled_dates)
# print(rule.__dict__)
