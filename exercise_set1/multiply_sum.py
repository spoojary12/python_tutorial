def multiply_sum(num1,num2):
    product=num1*num2
    if product<=1000:
      return product
    else:
      return num1+num2
result=multiply_sum(20,30)
print(result)
result=multiply_sum(30,40)
print(result)