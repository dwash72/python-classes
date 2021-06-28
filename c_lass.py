class Workers:
	"""docstring for emp"""
	def __init__(self, first, last, email):
		self.first = first
		self.last = last
		self.email = email
class develops(Workers):
	"""docstring for develops"""
	def __init__(self, first, last, email, field):
		super().__init__(first, last, email)
		self.field = field
d1 =develops('dwash', 'm', 'dwash@gmail.com', 'python programmer')
print(d1.first)
print(d1.last)
print(d1.email)
print(d1.field)