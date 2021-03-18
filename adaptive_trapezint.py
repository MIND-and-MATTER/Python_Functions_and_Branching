# Make an adaptive Trapezoidal rule
from math import cos, sin, pi;

#def adaptive_trapezint(f, a, b, eps=1E-5):


def trapezintad(f, a, b, n=10):
  h = (b-a) / n 
  A = h / 2  
  val = 0
  for i in range(0, n):
    xi = a + i * h
    val += f(xi) + f(xi + h)
  return A * val   

print(f"{trapezintad(sin, 0, pi/2, 1000):.2f}")
