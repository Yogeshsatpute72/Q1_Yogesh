
def get_factors(n):
    i = 1
    factors = set()
    while i*i <= n:
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
        i += 1

    return factors


j = int(input())

if j <= 0:
    print("Please provide a valid positive integer")
    exit
else:
    count = tuple(filter(lambda x : len(get_factors(x)) > 3, range(1, j+1)))
    print(len(count))

