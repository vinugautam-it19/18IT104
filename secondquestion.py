a=int(input())
b=int(input())
c=int(input())
def fizz_buzz(x):
  if((x%3==0)and(x%5==0)):
    c="FizzBuzz"
  elif(x%3==0):
    c="Fizz"
  elif(x%5==0):
    c="Buzz"
  else:
    c=x
  return c;
print(fizz_buzz(a))
print(fizz_buzz(b))
print(fizz_buzz(c))
