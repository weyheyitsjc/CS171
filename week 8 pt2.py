def gen_prime_num(upper_bound):
    for i in range(2, upper_bound + 1):
        for j in range(i - 1, 0, -1):
            if i % j == 0:
                break
            if j == 2:
                print(i, 'is a prime number')
                
gen_prime_num(3)