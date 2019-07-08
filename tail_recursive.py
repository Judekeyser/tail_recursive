# This is the module file for the implementation of tail recursion in Python

class ContinueState:
	pass


class Proxy:
	def __init__(self, wrapped):
		self.first_time = True
		self.wrapped = wrapped
		self.CONTINUE = ContinueState()
		self.stored_args = None
		self.stored_kwargs = None
	
	def do(self, args, kwargs):
		self.stored_args = args
		self.stored_kwargs = kwargs
		if self.first_time:
			self.first_time = False
			x = self.CONTINUE
			while x == self.CONTINUE:
				x = self.wrapped(*self.stored_args, **self.stored_kwargs)
			self.first_time = True
			return x
		return self.CONTINUE


def tail_recursive(f):
	proxy = Proxy(f)
	def g(*args, **kwargs):
		return proxy.do(args, kwargs)
	return g

