def natural(x):
    sum = 0
    for i in range(0,x):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

print natural(1000)