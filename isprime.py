def isPrime(num): # num: parametre
  if num<2:   # 2 den küçükse asal değil
    return False
  elif num != int(num):  # ondalık sayı ise asal değil
    return False
  else:  # normal bir sayının testi
    divNum = 0
    for i in range(2,num-1):
      if (num%i == 0):
        divNum = divNum + 1
    if divNum == 0:
      return True
    else:
      return False
##############################################################
def allPrimes(n):
  lst = []
  for i in range(2,n):
    if isPrime(i):
      lst.append(i)
  return lst
##############################################################
n1 = 20
print(isPrime(n1)) # n1 değişkeni argüman dır

n2 = 100
lst2 = allPrimes(n2)
print(lst2)
