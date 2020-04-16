def adjacentElementsProduct(inputArray):
    max_ = inputArray[0]*inputArray[1]
    for i in range(1,len(inputArray)-1):
      pr = inputArray[i]*inputArray[i+1]
      if pr > max_:
        max_ = pr
    return max_

inputArray = [3, 6, -2, -5, 7, 3]
print(adjacentElementsProduct(inputArray)) # ekran: 21 olmalı, çünkü 7*3=21

def adjacentElementsProduct2(inputArray):
    lst = []
    for i in range(1,len(inputArray)-1):
      lst.append(inputArray[i]*inputArray[i+1])
    return lst
  
lst2 = adjacentElementsProduct2(inputArray)
print(lst2,max(lst2))
