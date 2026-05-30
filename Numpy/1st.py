temperature = [32.5,43.4,43.2,43.3,35.5]

total = 0

for temp in temperature:
    total += temp

average = total/len(temperature)
print(average)