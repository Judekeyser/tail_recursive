# tail_recursive

This is a small module to implement tail recursive algorithm in the Python programming language.

Tail recursivity: short introduction
------------------------------------

Consider the problem of resolving the Newton iterative algorithm
```latex
\[ x_0 = 1 \]
\[ x_{k+1} = \frac{1}{2} \big( x_k + \frac{2}{x_k} \big) \]
```

The method is known to converge to the square root of 2.
A naive implementation is to program it using a recursive function:

```python
def f(stack, k):
	if k == 1:
		return stack
	stack = 0.5 * (stack + 2/stack)
	return f(stack, k-1)

approximation = f(1, 100)
```

This piece of script will give you a quite accurate approximation of the square root of 2.
Under the hood, the computer needs to call your function a hundrer time before returning a single value.
This is because the function calls itself. In the meantime, a call to a function leaves a scope opened
until the next call has returned something. At the end, you end up with a hundrer of opened stacks.

For Python, this is not a great problem. But what if the iterative method was so slow that 100 iterations was
not enough? Changing 100 to 1000 is likely to give you a `RecursionError`: leaving opened to many stack requires the
computer to need more and more memory, which is not always desirable (or possible).

Here comes the **tail recursion optimization**. In fact, you noticed that we do not require to perform
any computation after the last call of `f`. More precisely: there is no need to leave the stack opened at the end of the
function, as we are not going to do anything with the result. The tail recursion optimization is an compilation process
that allows you to, somehow: automatically close the stacks.

Python lack of implementation
-----------------------------

Unfortunately, the Python programming language does not provide any support for tail recursion.
After a quick search on a search engine, you realize that implementing tail recursion requires you to change the
syntax of your function: at this point, you could for the same prize replace you recursive method by some while loop...

We provide a simple module to implement tail recursion.
The tail recursivity of a method is indicated by the use of a decorator:

```python
@tail_recursive
def f(stack, k):
	if k == 1:
		return stack
	stack = 0.5 * (stack + 2/stack)
	return f(stack, k-1)
```

Any trial to make a computation with the result of the last line would fail to a syntax error:
```python
@tail_recursive
def f(stack, k):
	if k == 1:
		return stack
	stack = 0.5 * (stack + 2/stack)
	return 1 * f(stack, k-1)  # fails to compile
```

This is expected for tail recursion. On the other hand, the code now performs for a large number of iterations.

Small benchmarks and stack test
-------------------------------

the `main.py` function shows some small results that let you appreciate the decorator:
```text
---------------------
Main class
---------------------
Looping with 900 stacks
Ellapsed time for recursion, 10000 steps: 0.2655048370361328
Ellapsed time for tail recursion, 10000 steps: 9.297344207763672
---------------------
Looping with 1000 stacks
Computation failed for recursive method: max stack
Computation done for tail recusrive method; ellapsed time: 0.0
---------------------
```

How it works
------------

The decorator `tail_recursive` replaces the provided method reference by the `apply` method of
some `Proxy` object. The `Proxy` object is made such that it breaks the recursive step
written in the original code, and replace it by some `while` loop.

No reflection nor code rewritting is used in the process.
