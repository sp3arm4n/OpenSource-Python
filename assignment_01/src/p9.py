f1 = open("alkaline_metals.txt", "r")

atomic_numbers = []
atomic_weights = []

for line in f1:
    atomic_number, atomic_weight = line.split()
    atomic_numbers.append(atomic_number)
    atomic_weights.append(atomic_weight)

print("atomic_number", end='')
print(atomic_numbers)

print("atomic_weight", end='')
print(atomic_weights)