import time

def is_palindrome(num):
    centre = len(num) // 2
    for digit in range(centre + 1):
        if num[digit] != num[-digit - 1]:
            return False
    return True

def is_product(num):
    for p in range(100, 999) :
        if num % p == 0 :
            d = num / p
            if (d > 99 and d < 1000) :
                return True
    return False

def find_largest_palindrome(minNum, maxNum):
    for i in range(maxNum, minNum, -1):
        if is_palindrome(str(i)) and is_product(i):
            return i
    return minNum
        
# min 100x100, max 999x999=998001 which means max palindrome is then 997799
start = time.time()
print('Largest palindrome: ', find_largest_palindrome(10001, 997799))
end = time.time()
print('Duration:', round((end - start) * 1000, 2), 'ms')

