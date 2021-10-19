from datetime import datetime, date, timedelta

def within_allowed_days(slot:datetime, promo_datetime, gap_days):
    omin = promo_datetime - timedelta(days=gap_days)
    omax = promo_datetime + timedelta(days=gap_days)
    print(slot, '\n',omin, '|', promo_datetime, '|', omax)
    if omin <= slot <= omax:
        return False
    return True

dt_list = [datetime(2021,10,22,18), datetime(2021,10,22,20), datetime(2021,10,23,18), datetime(2021,10,23,20)]



print(within_allowed_days(datetime(2021,10,21,15), dt_list[0], 1))