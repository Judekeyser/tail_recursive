import time
from tail_recursive import tail_recursive


def f(stack, k):
	"""
	Fake tail recursive function
	"""
	if k == 1:
		return stack
	stack = 0.5 * (stack + 2/stack)
	return f(stack, k-1)

@tail_recursive
def g(stack, k):
	"""
	'True' tail recursive function
	"""
	if k == 1:
		return stack
	stack = 0.5 * (stack + 2/stack)
	return g(stack, k-1)


if __name__ == '__main__':
	print("---------------------")
	print("Main class")
	print("---------------------")
	print("Looping with 900 stacks")
	t1 = time.time()
	for i in range(0,10000):
		f(1, 900)
	t2 = time.time()
	z1 = t2 - t1
	t1 = time.time()
	for i in range(0,10000):
		g(1, 900)
	t2 = time.time()
	z2 = t2 - t1
	print("Ellapsed time for recursion, 100 steps:", z1)
	print("Ellapsed time for tail recursion, 100 steps:", z2)
	print("Speed gain: ", str(z1/z2 * 100 - 100)+"% of gain")
	print("---------------------")
	print("Looping with 1000 stacks")
	try:
		f(1, 1000)
		print("Computation done for recusrive method")
	except:
		print("Computation failed for recursive method: max stack")
	try:
		t1 = time.time()
		g(1, 1000)
		t2 = time.time()
		z = t2-t1
		print("Computation done for tail recusrive method; ellapsed time:", z)
	except:
		print("Computation failed for tail recursive method: max stack")
	print("---------------------")
	print("Looping with 50.000 stacks")
	try:
		f(1, 50000)
		print("Computation done for recusrive method")
	except:
		print("Computation failed for recursive method: max stack")
	try:
		t1 = time.time()
		g(1, 50000)
		t2 = time.time()
		z = t2-t1
		print("Computation done for tail recusrive method; ellapsed time:", z)
	except:
		print("Computation failed for tail recursive method: max stack")
	