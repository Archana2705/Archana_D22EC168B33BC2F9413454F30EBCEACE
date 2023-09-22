def LinearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices. append(index)

  return indices

#example
product = ["shoes" , "boot" , "loafer" , "shoes" , "sandal" , "shoes"]
target= "shoes"
result=LinearSearchProduct(product ,target)
print(result)
