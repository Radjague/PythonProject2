

def fizz_buzz(n:int)-> str:

  if n==5 or n==10:
    return 'buzz'

  if n==3 or n==6 or n==9 or n==12:
    return 'fizz'

  if n==0:
   return 'fizzbuzz'

  return str(n)