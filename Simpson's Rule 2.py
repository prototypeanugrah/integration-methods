" only integrable for equally spaced divisions divisible by THREE between the intervals [a,b] "


def f(x):
  return (x**2 - 3*x)

def solve(a,b,n):
  h = float(b-a)/n
  i = 1
  s = f(a)
  
  if(n%3 == 0):
    
    while(i <= (n/3)):
        s = s + 3*f(a + (3*i-2)*h) + 3*f(a + (3*i-1)*h) + 2*f(a + 3*i*h)
        i = i+1 
  
    s = s - f(a + 3*(i-1)*h)
    return abs(3*h*s/8)
  
  else:
    n = int(input("enter value of n divisible by 3"))
    return solve(a,b,n)
  
