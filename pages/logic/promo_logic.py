
class Post():
	def __init__(self, placement, goal, price:float):
		self.placement = placement
		self.goal = goal
		self.price = price

class PostsList():
	def __init__(self):
		self.posts = []

	def add(self, post:Post, amount):
		if len(self.posts) > 0:
			for p in self.posts:
				if post.goal == p[0].goal and post.placement == p[0].placement:
					raise ValueError(f"Conflicting post list values. Placement '{post.placement}' with goal '{post.goal}' already exists.")
			self.posts.append([post, amount])					
		else: 
			self.posts.append([post, amount])

	def add_many(self, posts_data):
		for pd in posts_data:
			self.add(pd[0], pd[1])

	def print_list(self):
		for p in self.posts:
			print(p[1], p[0], p[0].goal, p[0].placement, p[0].price)

class DiscountTable():
	def __init__(self, data, bundle_discount=0):
		'''
		data = [(posts_amount1, discount1), (posts_amount2, discount2), ...]

		For now discounts are unidimensional, that means that the bulk discount applies to all posts kinds and goals only based on the amount
		To improve this, I should add more granular control over what discount value applies to what post kind and goal
		'''
		self.dtable = sorted(data)
		self.bundle_discount = self.set_bundle_discount(bundle_discount)

	def get_bulk_discount(self, posts_amount):
		for idx, d in enumerate(self.dtable):
			if d[0] == 0: # (0,0) or (o, number) affects the logic so we skip that step if it is found
				continue
			print(posts_amount, d[0])
			if posts_amount >= d[0]:
				return d[1]
		return 0

	def set_bundle_discount(self, bundle_discount):
		if (bundle_discount > 1):
			bundle_discount /= 100
		return bundle_discount

class PromoPackage():
	def __init__(self, posts_data, discount_table:DiscountTable):
		'''
		data = [(amount1, Post Type obj1), (amount2, Post Type obj2)]
		'''
		self.posts_data = posts_data
		self.dt = discount_table
		self.package, self.placements = self.make_package(self.posts_data)
		self.prices = self.make_prices(self.posts_data)
		self.summary, self.total, self.discount_total = self.make_summary(self.package)
		

	def make_package(self, posts_data):
		package = {
					'growth': {}, 
					'sales': {}
					}

		placements = []
		
		for d in posts_data:
			amount = d[1]
			post_obj = d[0]

			# to check if it's a bundle later (if 2 kinds are in the package then a bundle discount can be applied)
			placement = post_obj.placement
			if placement not in placements:
				placements.append(placement)

			if post_obj.placement in package[post_obj.goal]:
				package[post_obj.goal][post_obj.placement] += amount
			else:
				package[post_obj.goal][post_obj.placement] = amount
			
		return package, placements

	def make_prices(self, posts_data):
		prices = {
					'growth': {}, 
					'sales': {}
				}
		for d in posts_data:
			# amount = d[1]
			post_obj = d[0]
			if post_obj.placement in prices[post_obj.goal]:
				prices[post_obj.goal][post_obj.placement] += post_obj.price
			else:
				prices[post_obj.goal][post_obj.placement] = post_obj.price
		return prices
	
	def make_summary(self, package):
		summary = ''
		grand_total = 0
		discounted_total = 0
		for goal in package.keys():
			for placement, amount in package[goal].items():
				price = self.prices[goal][placement]
				
				bundle_discount = 0
				if len(self.placements) >= 2:
					bundle_discount = self.dt.bundle_discount

				bulk_discount = self.dt.get_bulk_discount(amount)
				

				# overlapping discounts formula = p ( 1 - d1 - d2 - d1d2 ), where p is the price, d1 & d2 the discounts
				price_final = price * (1 - bulk_discount - bundle_discount - bulk_discount * bundle_discount) * amount
				price_discounted = price * ( bulk_discount + bundle_discount + bulk_discount * bundle_discount ) * amount
				grand_total += price_final
				discounted_total += price_discounted 
				summary += f'{amount} x {goal}-{placement} - {price_final} (from {price*amount})\n'
		return summary, grand_total, discounted_total
		

if __name__ == "__main__":
	dt = DiscountTable([[0,0], [3,15], [6,25]], bundle_discount=0.2)
	p1 = Post('story', 'growth', 25)
	p2 = Post('feed', 'growth', 20)
	pl = PostsList()
	pl.add_many( [ (p1, 3)] )
	pp = PromoPackage(pl.posts, dt)
	# print(pp.summary, pp.total, pp.discount_total)
	print(dt.get_bulk_discount(2))  