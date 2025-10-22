

def fizz_buzz(n:int)-> str:
  if n % 3==0 and n % 5==0:
    return 'fizzbuzz'
  if n % 5==0:
    return 'buzz'

  if n % 3==0 :
    return 'fizz'

  return str(n)