def shapeArea(n):
  return int((2*n-1)**2 - 4*(n-1)*n/2)

def shapeArea2(n):
  area = 0
  for i in range(1,n):
    area = area + 2*i-1
  return 2*n-1 + 2*area

n = 3
print(n,shapeArea2(n))
