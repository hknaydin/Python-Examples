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
  
allPrimes(100)first_coeff = 0.5   # arasınav katsayısı
final_coeff = 0.5   # final katsayısı

first_grade = 78    # arasınav notu
final_grade = 65    # final notu

######################################

# aşağıdaki kodu tamamlayınız

avg_grade = int(first_coeff*first_grade) + int(final_coeff*final_grade)


######################################

'''

0-45    FF
45-53   CC
53-61   CB
61-69   BB
69-77   BA
77-100  AA
'''

if avg_grade < 45 :
  grade_word = "FF"
  print ("kaldiniz")
elif  avg_grade <53 :   
  grade_word = "CC"
elif avg_grade < 61 :   
  grade_word = "CB"
elif avg_grade< 69 :   
  grade_word = "BB"
elif avg_grade <77 :   
  grade_word = "BA"
else : 
 grade_word = "AA"

print ("harf notunuz", grade_word)
