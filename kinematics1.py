# Compute velocity and acceleration from 1D position data
import numpy as np; 

def kinematics(x, i, dt=1E-6):

  n = len(x) 
  t = [0]
  v_list = []
  a_list = []
  
  

  for i in range(1, n):
    t.append(t[-1]+dt)

  for i in range(1, n-1):

    v_num = x[i + 1] - x[i-1]
    v_den = t[i+1] - t[i-1]

    vi = v_num / v_den 

    a_fact = 2 / (t[i+1] - t[i-1])
    a_num1 = (x[i+1] - x[i])
    a_den1 = (t[i+1] - t[i])
    a_num2 =  (x[i] - x[i-1])
    a_den2 = (t[i] - t[i-1])

    ai = a_fact * ((a_num1/a_den1) - (a_num2/a_den2))
    
    v_list.append(vi)
    a_list.append(ai)

  return a_list
  return list(zip(v_list, a_list))
  
q = [1, 5, 3, 4, 5]
print(kinematics(q, 5))

def test_kinematics():
  a_list = []
  kinematics(q,5)


  if sum(a_list) == 0:
    print("Velocity of the object is constant.") 
  else:
      print("The object is accelerating/decelerating")

print(test_kinematics())

    