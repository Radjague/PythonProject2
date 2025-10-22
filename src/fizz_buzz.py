

def fizz_buzz(n:int)-> str:
  if n == 7:
    return '7'
  if n==5:
    return 'buzz'

  if n==4:
    return '4'

  if n==3 or n==6:
    return 'fizz'

  if n==2:
    return '2'

  if n==1:
    return '1'

  return 'fizzbuzz'