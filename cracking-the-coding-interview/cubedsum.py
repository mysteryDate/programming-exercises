MAX_VAL = 1000
sum_map = {}

for a in range(MAX_VAL):
    for b in range(a, MAX_VAL):
        if a == b:
            continue
        cubed_sum = a ** 3 + b ** 3
        sum_map[cubed_sum] = (a, b)

for c in range(MAX_VAL):
    for d in range(c, MAX_VAL):
        if c == d:
            continue
        cubed_sum = c ** 3 + d ** 3
        if cubed_sum in sum_map:
            a, b = sum_map[cubed_sum]
            if a != c and a != d and b != c and b != d:
                print("{a}, {b}, {c}, {d}".format(a=a, b=b, c=c, d=d))
