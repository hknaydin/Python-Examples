def shapeArea(rows):
  for i in range(rows):
    print(" "*(rows-i-1)+'* '*(i+1))
  for i in range(rows-1):
    print(' '*(i + 1) + "* "*(rows - i - 1))

  
shapeArea(3) # ekrana n=3 için olan şekli çizecek ve toplam alan=13 yazacak
shapeArea(4) # ekrana n=4 için olan şekli ve toplam alan=25 yazacak
shapeArea(7) # benzer şekilde çıktı vermeli
