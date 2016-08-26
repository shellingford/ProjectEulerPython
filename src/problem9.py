import time

def product_abc(limit):
    #a < b < c
    for a in range(1, limit//3):
        for b in range(a + 1, limit // 2):
            c = limit - a - b
            if c**2 == (a**2 + b**2):
                return a*b*c
    return -1 #shouldn't happen

start = time.time()

print('Product is: ', product_abc(1000))

end = time.time()
print('Duration:', round((end - start) * 1000, 2), 'ms')