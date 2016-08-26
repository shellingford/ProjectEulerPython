import time

def fib_index(digit_limit):
    a = 1
    b = 1
    i = 1
    while len(str(a)) != digit_limit:
        p = a
        a = b
        b = p + b
        i += 1
    return i 
start = time.time()

print('Index of the first term in the Fibonacci sequence to contain 1000 digits is: ', fib_index(1000))

end = time.time()
print('Duration:', round((end - start) * 1000, 2), 'ms')
