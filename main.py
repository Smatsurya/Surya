def fast_rect(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rect(n-1) 
number=int(input ('enter the factorial number in int '))
result=int(fact rect(number))
print("the factorial of{} is {} ".format(number,result))