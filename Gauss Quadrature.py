


import numpy
from numpy.polynomial.legendre import leggauss

def f(x):
  f= 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5
  return f

def solve(a,b,n):
  
  x,w = leggauss(n)
  ps=0
  for i in range(n):
    ps = ps + w[i]*f(0.5*((b+a) + (b-a)*x[i]))
  
  gi = 0.5*(b-a)*ps

  return gi
  
  
