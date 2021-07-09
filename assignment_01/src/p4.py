first = [1, 2, 3, 4]
second = [1, 2, 3, 4]

def dot_product(a, b):
    c = []
    for k in range(0, len(a)):
        c.append(a[k] + b[k])
    return c

third = dot_product(first, second)

print(third)