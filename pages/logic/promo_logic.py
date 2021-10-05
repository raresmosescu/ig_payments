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
	def __init__(self, objective, pnum:list):
		# pnum: list of tupls with placements and number of posts 
		# e.g. [('story', 10), ('feed', 5)]
		self.objective = objective
		self.placements, self.numbers = zip(*pnum) # unzip the list 
		# pnum = [('story', 10), ('feed', 5)] with * becomes ('story', 10), ('feed', 5)
		self.pnum = pnum

	def total(self):
		for p, n in self.pnum:
			print(p,n)

class Price():
	def __init__(self, objective, placement, price_per_post, dnum):
		# discounts per number of posts (e.g. (10 posts, $10 off per post))
		self.placement = placement
		self.price_per_post = price_per_post
		self.dnum = dnum

class PriceList():
	def __init__(self, price_list = None) -> None:
		if price_list == None:
			self.list = price_list
		else:
			self.list = []


promo = Promotion(objective='sales', pnum=[('story', 10), ('feed', 5)])
price = Price('sales', 'story', 25, [(1, 0), (3, 5)])