threshold = float(input())
n = int(input())

total = 0
errors = 0
exceeded = 0
sum_temp = 0.0
count_ok = 0
maximum = None

for i in range(n):
    line = input().strip()
    total += 1

    if line == "error":
        errors += 1
        continue

    value = float(line)
    count_ok += 1
    sum_temp += value

    if value > threshold:
        exceeded += 1

    if maximum is None or value > maximum:
        maximum = value

average = sum_temp / count_ok

print()
print(total)
print(errors)
print(exceeded)
print(f"{maximum:.1f}")
print(f"{average:.1f}")