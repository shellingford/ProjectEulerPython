import time

start = time.time()

#sum of square: n(n+1)(2n+1)/6
#square of sum: n(n+1)/2
#diff: n(n+1)(3n+2)(n-1)/12
diff = 100*101*302*99/12

print('Difference: ', diff)

end = time.time()
print('Duration:', round((end - start) * 1000, 2), 'ms')