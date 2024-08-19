import math 
# if n is less than 2, not prime, otherwise iterate through all
# numbers up to the sqrt of n to see if they are a factor, if not, n is prime
def is_prime(n):
  if n < 2:
      return False
  i = 2
  while i*i <= n:
      if n % i == 0:
          return False
      i += 1
  return True


def largest_prime_factor(n):
    for i in range (2, n):
        while n % i == 0:
            n //= i
        if is_prime(n):
            break 
    return(n)
         
    
print(largest_prime_factor(600851475143))

        
    
  