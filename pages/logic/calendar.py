from datetime import datetime, date, time
from promo_logic import Promotion
from pprint import pprint

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
        self.scheduled_datetimes = {
            'feed': [],
            'story': []
        }
        self.scheduled_promos = []

    # adds a single date to a placement
    def add(self, datetime:datetime, placement, auto_sort=True):
        if self.is_unavailable(datetime, placement):
            raise ValueError(f'Datetime "{datetime}" is not available for placement "{placement}".')
        self.scheduled_datetimes[placement].append(datetime)
        if auto_sort:
            self.sort(placement)

    # adds many dates to a placement
    def add_many(self, datetimes:list, placement):
        if placement not in ['story', 'feed']:
            raise ValueError(f'Placement "{placement}" is not supported.')
        for datetime in datetimes:
            self.add(datetime, placement, auto_sort=False)
        self.sort(placement)
    
    # removes a date from a placement
    def remove(self, datetime:datetime, placement):
        self.scheduled_datetimes[placement].remove(datetime)

    # checks if a datetime is already used for a placement
    def is_unavailable(self, datetime:datetime, placement):
        if datetime in self.scheduled_datetimes[placement]:
            return True
        return False

    # sorts the placement, if provided, else sorts all placements
    def sort(self, placement=''):
        if placement:
            self.scheduled_datetimes[placement] = sorted(self.scheduled_datetimes[placement])
        else:
            self.scheduled_datetimes = {k:sorted(v) for k,v in self.scheduled_datetimes.items()}

    # adds a Promotion object and processes it
    def add_promotion(self, promo:Promotion):
        self.scheduled_promos.append(promo)
        self.add_many(promo.datetimes['story'], 'story')
        self.add_many(promo.datetimes['feed'], 'feed')

    def get_datetimes_by_placement(self, placement):
        return self.scheduled_datetimes[placement]

    # returns a list with all unconfirmed promotions
    def get_unconfirmed_promos(self):
        return [p for p in self.scheduled_promos if not p.is_confirmed]

    # returns a list with all confirmed promotions
    def get_confirmed_promos(self):
        return [p for p in self.scheduled_promos if p.is_confirmed]

    def get_promo_num_for_date(self, dt1:datetime, placement:str):
        c = 0
        for dt2 in self.scheduled_datetimes[placement]:
            if dt2.date() == dt1.date():
                c+=1
        return c






# testing
if __name__ == '__main__':
    cal = Calendar()

    story_dates = [
        datetime(2021,10,20,18,0), datetime(2021,10,20,15,0),
        datetime(2021,10,21,18,0), datetime(2021,10,21,15,0)
    ]

    feed_dates = [
        datetime(2021,11,20,18,0), datetime(2021,11,20,15,0),
        datetime(2021,11,21,18,0), datetime(2021,11,21,15,0)
    ]

    p = Promotion(objective='sales', pnum=[('story', 4), ('feed', 4)])
    p.datetimes['story'] = story_dates
    p.datetimes['feed'] = feed_dates
    cal.add_promotion(p)

    pprint(cal.scheduled_datetimes)
    pprint(cal.get_unconfirmed_promos())

    print(f'Total promos on date {datetime(2021,10,20).date()}: {cal.get_promo_num_for_date(datetime(2021,10,20), "story")}')
