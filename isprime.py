def isPrime(num):
  divisorNumber = 0
  # burada num sayısının bölen sayısını bulunuz.
  # ...,
  for i in range(2,int(num)):
    if num % i == 0:
      divisorNumber = divisorNumber + 1

  if divisorNumber == 0:
    return True
  else:
    return False

n1 = 19
print(n1,isPrime(n1))  # ekran: 19, True olmalı

##############################################################

def allPrimes(n):
  lst = []
  for i in range(2, n) :

    if isPrime(i) :
      lst.append(i)
  print(lst)
  
allPrimes(100)
