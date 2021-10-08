from datetime import datetime, date, time

# datetime.combine(date.today, time(10,30))

promo_request = {
    'objective': 'sales',
    'pnum': [('feed', 6), ('story', 6)]
}

class Promo():
    def __init__(self, d:date, t:time):
        self.d = d

scheduled = [Promo(date.today()), Promo(date.today())]

promo = Promo()

unavailable_dates = [date(), date()]
offset_day = 1
posts_per_day = 2
starting_day = date()