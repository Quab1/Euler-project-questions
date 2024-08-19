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

# iterate through all numbers up till n/2+1 to find a factor of n to divide n by to 
# make smaller until largest prime factor
def largest_prime_factor(n):
    for i in range (2, n):
         
    
print(largest_prime_factor(52))

        
    
  