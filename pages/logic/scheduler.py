from datetime import datetime, date, time, timedelta
from typing import Generator
from promo_logic import Promotion, PriceList, Price, Pricing
from calendar import Calendar
from pprint import pprint


# handles rules which tell the generator how to generate the available dates list
class PageGeneratorRules():
	def __init__(self, daily_available_times:list=None, posts_per_day:dict = {}, gap_days:int = 0, gap_hours:int = 0, notice_time:int=0) -> None:		
		if daily_available_times != None:
			self.daily_available_times = sorted(daily_available_times)
		else:
			daily_available_times = []

		self.posts_per_day = {
			'story': 0,
			'feed': 0
		}
		if self.posts_per_day:
			self.posts_per_day['story'] = posts_per_day['story']
			self.posts_per_day['feed'] = posts_per_day['feed']
		else:
			self.posts_per_day['story'] = len(self.daily_available_times)
			self.posts_per_day['feed'] = len(self.daily_available_times)


		# neighboring days are blocked and only one post per day is allowed if this has a value greater than 0
		self.gap_days = gap_days 
		if self.gap_days:
			self.posts_per_day['story'] = 1
			self.posts_per_day['feed'] = 1

		self.gap_hours = gap_hours # neighboring hours are blocked
		self.notice_time = notice_time # min time from the moment of promo request to the posting date

class ScheduleGenerator():
	def __init__(self, promo:Promotion, cal:Calendar, rules:PageGeneratorRules = None) -> None:
		self.promo = promo
		self.cal = cal
		self.rules = rules    
		self.datetimes = {
			'feed': [],
			'story': []
		}    
		self.blocked_datetimes = {
			'feed': [],
			'story': []
		}   
	# get the last datetime in list and return the result of counting how many consecutive datetimes have the same day 
	# in reverse order, from last to first item
	def get_generated_dt_for_date(self, dt1:datetime, dt_list:list):
		c = 0
		for dt2 in dt_list:
			if dt1.date() == dt2.date():
				c+=1
		return c

	# checks if date is not within now->now+notice_minutes 
	def within_notice_time(self, slot:datetime, notice_minutes:int):
		delta = slot - datetime.now()
		# print(delta)
		if delta.days == 0 and delta.seconds/60 > notice_minutes or delta.days > 0:
			return True
		else:
			return False

	def within_allowed_days(self, slot:datetime, promo_datetime, gap_days):
		omin = promo_datetime - timedelta(days=gap_days)
		omax = promo_datetime + timedelta(days=gap_days)
		if omin < slot < omax:
			return False
		return True

	def within_allowed_hours(self, slot:datetime, promo_datetime, hours_offset=3.5):
		omin = promo_datetime - timedelta(seconds=hours_offset*60*60)
		omax = promo_datetime + timedelta(seconds=hours_offset*60*60)
		# print(omin, '|', slot, '|', omax)
		if omin < slot < omax:
			# print("FALSE")
			return True
		# print("TRUE")
		return True

	def check_calendar(self, slot:datetime, placement:str, cal:Calendar, rules:PageGeneratorRules, dt_list:list):
		if rules.gap_days: # for this mode, most rules change (refer to PageGeneratorRules class to see how)
			
			for promo_datetime in cal.scheduled_datetimes[placement]:
				# if datetime is found within the unallowed range for scheduled promotions datetimes
				if not self.within_allowed_days(slot, promo_datetime, rules.gap_days):
					return False
			for generated_datetime in dt_list:
				# if datetime is found within the unallowed range for currently generated datetimes
				if not self.within_allowed_days(slot, generated_datetime, rules.gap_days):
					return False
			if ( cal.get_promo_num_for_date(slot, placement) + self.get_generated_dt_for_date(slot, dt_list) ) >= rules.posts_per_day[placement]:
				# print('TOO MANY POSTS PER DAY', cal.get_promo_num_for_date(slot, placement) + self.get_generated_dt_for_date(slot, dt_list), dt_list)
				return False
		else:
			
			for promo_datetime in cal.scheduled_datetimes[placement]:
				# if datetime is found within the unallowed range
				if not self.within_allowed_hours(slot, promo_datetime):
					return False
			# if number of promos in this date + number of promos with a date generated in this date is >= 
			# than the max number of posts per day - 1 return False (max number of posts on this date was reached)
			if ( cal.get_promo_num_for_date(slot, placement) + self.get_generated_dt_for_date(slot, dt_list) ) >= rules.posts_per_day[placement]:
				# print('TOO MANY POSTS PER DAY', cal.get_promo_num_for_date(slot, placement) + self.get_generated_dt_for_date(slot, dt_list), dt_list)
				return False	
		return True	

	def slot_available(self, slot:datetime, placement:str, rules:PageGeneratorRules, dt_list:list):
		if (self.within_notice_time(slot, rules.notice_time) and
		self.check_calendar(slot, placement, cal, rules, dt_list)):
			return True
		return False

	def generate_datetimes(self, n, rules:PageGeneratorRules, placement='story'):
		dt = datetime.now()
		res = []
		while len(res) <= n:
			# generates datetimes for each available time the page has set per day
			daily_slots = [datetime.combine(dt.date(), t) for t in rules.daily_available_times]
			# then checks each slot to see if it's available based on the rules and existing promotions
			for slot in daily_slots:
				if len(res) == n:
					return res
				if self.slot_available(slot, placement, rules, res):
					res.append(slot)
			dt = dt + timedelta(days=1)
		return res

if __name__ == '__main__':

	prices = PriceList([
		#     objective, placement, price per post, list with discounts / number of posts = [ (min number of posts, discount), ... ]
		Price('sales', 'story', 25, [(0, 1), (5, 3)]), 
		Price('sales', 'feed', 60, [(0, 1), (10, 3)]),
		Price('growth', 'story', 25, [(0, 1), (5, 3)]),
		Price('growth', 'feed', 20, [(0, 1), (5, 3)])
		])
	p = Promotion(objective='sales', pnum=[('story', 10), ('feed', 5)])

	pr = Pricing(prices, p)


	cal = Calendar()

	story_dates = [
		datetime(2021,10,20,18,0), datetime(2021,10,20,15,0),
		datetime(2021,10,21,18,0), datetime(2021,10,21,15,0)
	]

	feed_dates = [
		datetime(2021,11,20,18,0), datetime(2021,11,20,15,0),
		datetime(2021,11,21,18,0), datetime(2021,11,21,15,0)
	]

	# p = Promotion(objective='sales', pnum=[('story', 4), ('feed', 4)])
	p.datetimes['story'] = story_dates
	p.datetimes['feed'] = feed_dates
	cal.add_promotion(p)

	rules = PageGeneratorRules(daily_available_times=[time(18), time(15), time(23), time(11)], posts_per_day={'story': 2, 'feed': 1}, gap_days=2, notice_time=0)
	# pprint(rules.posts_per_day)
	gen = ScheduleGenerator(p, cal, rules)
		
	dt = gen.generate_datetimes(10, rules)
	pprint(dt)
