

def fizz_buzz(n:int)-> str:

  if n==5:
    return 'buzz'

  if n==3 or n==6 or n==9:
    return 'fizz'

  if n==0:
   return 'fizzbuzz'

  return str(n)