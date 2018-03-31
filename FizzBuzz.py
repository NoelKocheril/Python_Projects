for i in range(120000000000):
  x = ""
  if(i%3 == 0):
    x+="Fizz"
  if(i%5 == 0):
    x+="Buzz"
  if(i%7 == 0):
    x+="Cuzz"
  if(i%11 == 0):
    x+= "Tuzz"
  if(x==""):
    print(i)
  else:
    print(x)
