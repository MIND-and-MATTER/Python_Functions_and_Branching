# Write a function for numerical differentiation
import math

q = lambda x: math.exp(x)
w = lambda x: math.exp(-2*x**2)
e = lambda x: math.cos(x)
r = lambda x: math.log(x)

def diff(f, x, h=1E-5):
  num = f(x+h) - f(x-h)
  den = 2*h
  fprime = num/den
  return fprime


def test_diff():
  def g(x):
    return  3*x**2 - 7*x + 2.5
  def g_prime(x):
    return 6*x - 7
  assert abs(diff(g, 3, 0.01) - g_prime(3)) <= 0.0001, "This function failed"
  
test_diff()

def application():
  print(f"{diff(q, 0, 0.01):.4f}")
  print(f"{diff(w, 0, 0.01):.4f}")
  print(f"{diff(e, math.pi*2, 0.01):.4f}")
  print(f"{diff(r, 1, 0.01):.4f}")

application()
