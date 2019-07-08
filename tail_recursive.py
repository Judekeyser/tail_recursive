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

	
	def do(self):
		while True:
			x = self.wrapped(*self.stored_args, **self.stored_kwargs)
			if not x == self.CONTINUE: break
		return x
	


def tail_recursive(f):
	proxy = Proxy(f)
	def g(*args, **kwargs):
		proxy.stored_args = args
		proxy.stored_kwargs = kwargs
		if not proxy.first_time: return proxy.CONTINUE
		proxy.first_time = False
		x = proxy.do()
		proxy.first_time = True
		return x
	return g


