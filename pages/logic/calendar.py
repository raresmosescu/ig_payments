from datetime import datetime, date, time
from promo_logic import Promotion

# # handles scheduled times
# class Day():
#     def __init__(self, datetime:datetime) -> None:
#         self.scheduled_times = []
#         self.date = date

#     def add(self, time:time):
#         self.scheduled_times.append(time)
#         self.sort()
        
#     def add_many(self, times:list):
#         self.scheduled_times += times
#         self.sort()

#     def sort(self):
#         self.scheduled_times = sorted(self.scheduled_times)

#     def remove(self, time:time):
#         self.scheduled_times.remove(time)

# handles scheduled promotions and their datetimes
class Calendar():
    def __init__(self) -> None:
        self.scheduled_datetimes = []
        self.scheduled_promos = []

    def add(self, datetime:datetime):
        self.scheduled_datetimes.append(datetime)
        self.sort()
        
    def add_many(self, datetimes:list):
        self.scheduled_datetimes += datetimes
        self.sort()
    
    def remove(self, datetime:datetime):
        self.scheduled_datetimes.remove(datetime)

    def sort(self):
        self.scheduled_datetimes = sorted(self.scheduled_datetimes)

    def add_promotion(self, promo:Promotion):
        self.scheduled_promos.append(promo)
        self.add_many(self, promo.dt)

    def get_unconfirmed(self):
        return [p for p in self.scheduled_promos if not p.is_confirmed]

    def get_confirmed(self):
        return [p for p in self.scheduled_promos if p.is_confirmed]



# testing
if __name__ == '__main__':
    cal = Calendar()
    # cal.add_many([datetime(2021, 10, 15, 18, 0), datetime(2021, 10, 12, 18, 0), datetime(2021, 10, 16, 18, 0)])
	# promo = 

    promos = [Promotion(objective='sales', pnum=[('story', 10), ('feed', 5)])]

    print(cal.scheduled_datetimes)
