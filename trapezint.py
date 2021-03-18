# Integrate a function by the Trapezoidal rule.
from math import cos, sin, pi;

def trapezint1(f, a, b):
  v = ((b - a) / 2) * (f(a) + f(b))
  return v


print(trapezint1(cos, 0, pi))
print(trapezint1(sin, 0, pi))
print(trapezint1(sin, 0, pi/2))

def trapezint2(f, a, b):
  v = ((b/2 - a) / 2) * (f(a) + f(b/2))
  v2 = ((b - b/2) / 2) * (f(b/2) + f(b))
  return v + v2

print(trapezint2(cos, 0, pi))
print(trapezint2(sin, 0, pi))
print(trapezint2(sin, 0, pi/2))

def trapezint(f, a, b, n=10):
  h = (b-a) / n 
  A = h / 2  
  val = 0
  for i in range(0, n):
    xi = a + i * h
    val += f(xi) + f(xi + h)
  return A * val 

print(f"{trapezint(cos, 0, pi, 1000):.2f}")
print(f"{trapezint(sin, 0, pi, 1000):.2f}")
print(f"{trapezint(sin, 0, pi/2, 1000):.2f}")


