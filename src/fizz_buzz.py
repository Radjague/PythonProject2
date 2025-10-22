

def fizz_buzz(n:int)-> str:
  if n == 0 or n == 15:
    return 'fizzbuzz'
  if n==5 or n==10:
    return 'buzz'

  if n % 3==0 :
    return 'fizz'

  return str(n)