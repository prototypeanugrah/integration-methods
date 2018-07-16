def f(x):
  return (x**2 - 3*x)

def solve(a,b,n):
  h=float(b-a)/n
  i=1
  fa = f(a)
  s = fa
  if(n % 2 == 0): 
    while(i<=(n/2)):
    
      s = s + 4 * f(a + (2*i-1)*h) + 2 * f(a + 2*i*h)
      i = i+1
      
  if(n % 2 == 0):
    s = s - f(a + 2*(i-1)*h)
    return abs(h * s / 3)

  else:
    print("enter even n")
