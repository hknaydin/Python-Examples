def divisorList(num):
  lst = []
  for i in range(1, num) :
    if num % i == 0:
      lst.append(i)
  return lst

n1 = 72
print("Birinci ornek", n1,divisorList(n1))

##################################################################
def isPerfect(num):
  lst = divisorList(num)
  if sum(lst[:-1]) == num:
    return True
  else:
    return False
##################################################################
def allPerfects(num):
  lst = []
  for i in range(1,num):
    if isPerfect(i):
      lst.append(i)
  return lst
##################################################################
n = 28
lst2 = divisorList(n)
print(lst2)

print(n,isPerfect(n))

n2 = 10000
lst3 = allPerfects(n2)
print(n2,"ye kadar olan mükemmel sayılar:",lst3)
