import time
from prime_util import primes

start = time.time()

print('Sum of all primes below 2M is: ', sum(primes(2000000)))

end = time.time()
print('Duration:', round((end - start) * 1000, 2), 'ms')