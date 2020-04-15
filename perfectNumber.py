def divisorList(num):
  lst = []
  for i in range(1, num) :
    if num % i == 0:
      lst.append(i)
  return lst

n1 = 72
print("Birinci ornek", n1,divisorList(n1))

##################################################################

def isPerfectNumber(num):
  lst = divisorList(num)
  lst_eleman_toplam = 0
  print(lst)

  for i in range (0,len(lst)):
    lst_eleman_toplam = lst_eleman_toplam + lst[i]
  
  if lst_eleman_toplam == num:
    return True
  else:
    return False
n1 = 28
print("İkinci ornek", n1,isPerfectNumber(n1))
