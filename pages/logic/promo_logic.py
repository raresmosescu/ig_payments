class Post():
	def __init__(self, ptype):
		self.ptype = ptype
		
class PostList():
	def __init__(self, post_list=None):
		if post_list == None:
			self.list = post_list
		else:
			self.list = []

	def _add(self, post:Post):
		self.list.append(post)

class Promotion():
	def __init__(self, objective, pnum:list, is_confirmed=False):
		# pnum: list of tupls with placements and number of posts 
		# e.g. [('story', 10), ('feed', 5)]
		self.objective = objective
		self.placements, self.numbers = zip(*pnum) # unzip the list 
		# pnum = [('story', 10), ('feed', 5)] with * becomes ('story', 10), ('feed', 5)
		self.pnum = pnum
		self.is_confirmed = is_confirmed

	def total(self):
		for p, n in self.pnum:
			print(p,n)

class Price():
	def __init__(self, objective, placement, price_per_post, dnum):
		# discounts per number of posts (e.g. (10 posts, $10 off per post))
		self.objective = objective
		self.placement = placement
		self.price_per_post = price_per_post
		# !!!!  dnum should be sorted from low to high for other classes to work properly
		self.dnum = sorted(dnum, key=lambda x: x[1])

class PriceList():
	def __init__(self, pricelist = None) -> None:
		if pricelist == None:
			self.list = []
		else:
			self.list = pricelist

class PromotionPrice():
	# the join of the 2 classes (Promotion and Price/PriceList) resulting in the prices of the promotion (total price, discounts used, etc)
	def __init__(self, objective, placement, price_per_post, number_of_posts, discount_per_post, price_obj):
		self.objective = objective
		self.placement = placement
		self.price_per_post = price_per_post
		self.number_of_posts = number_of_posts
		self.discount_per_post = discount_per_post
		self.price_obj = price_obj
		self.total = self.calculate_total()
		self.total_discount = self.calculate_total_discount()

	def calculate_total(self):
		return (self.price_per_post - self.discount_per_post) * self.number_of_posts

	def calculate_total_discount(self):
		return self.discount_per_post * self.number_of_posts

class Pricing():
	def __init__(self, all_prices:PriceList, promotion:Promotion = None):
		self.all_prices = all_prices
		self.promotion_prices = []
		if promotion == None:
			self.promotion = []
		else:
			self.promotion = promotion

	def add_promotion(self, promo:Promotion):
		self.promotion = promo
		self.calculate_prices(promo)

	def calculate_prices(self, promo:Promotion):
		for price in self.all_prices.list:
			if price.objective == promo.objective:
				for promo_pn in promo.pnum:
					promo_placement = promo_pn[0]
					promo_num = promo_pn[1]
					if promo_placement == price.placement:
						if promo_num >= price.dnum[-1][1]:
							# if promo_num is >= to the biggest package post number then append the biggest discount and promo_num
									self.promotion_prices.append(
										PromotionPrice(
											objective = promo.objective, 
											placement = promo_placement, 
											price_per_post = price.price_per_post, 
											number_of_posts = promo_num, 
											discount_per_post = price.dnum[-1][0], 
											price_obj = price
											)
										)						
						else:
							for price_discount, price_num in price.dnum:
								# price.dnum should be sorted from low to high
								if promo_num <= price_num:
									self.promotion_prices.append(
										PromotionPrice(
											objective = promo.objective, 
											placement = promo_placement, 
											price_per_post = price.price_per_post, 
											number_of_posts = promo_num, 
											discount_per_post = price_discount, 
											price_obj = price
											)
										)

	def total(self):
		total = 0
		for pp in self.promotion_prices:
			total += pp.total
		return total

	def describe_promo(self):
		if self.promotion == None:
			raise ValueError("No Promotion object exists. Add one using Pricing.add_promotion(Promotion) method.")
		total = 0
		total_discount = 0
		for idx, pp in enumerate(self.promotion_prices):
			total += pp.total
			total_discount += pp.total_discount
			print(f'[{idx}]: ${pp.total} - {pp.number_of_posts}x {pp.objective}-{pp.placement} (${pp.total_discount} OFF)')
		print('------------------------------')
		print(f'TOTAL: ${total} (${total_discount} OFF)')

if __name__ == '__main__':
	prices = PriceList([
		#     objective, placement, price per post, list with discounts / number of posts = [ (min number of posts, discount), ... ]
		Price('sales', 'story', 25, [(0, 1), (5, 3)]), 
		Price('sales', 'feed', 60, [(0, 1), (10, 3)]),
		Price('growth', 'story', 25, [(0, 1), (5, 3)]),
		Price('growth', 'feed', 20, [(0, 1), (5, 3)])
		])
	promo = Promotion(objective='sales', pnum=[('story', 10), ('feed', 5)])

	p = Pricing(prices, promo)
	p.add_promotion(promo)

	# print(p.promotion_prices)

	print(p.describe_promo())

