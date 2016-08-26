import time
from prime_util import primes


start = time.time()

print('10 001st prime number: ', primes(1000000)[10000])

end = time.time()
print('Duration:', round((end - start) * 1000, 2), 'ms')