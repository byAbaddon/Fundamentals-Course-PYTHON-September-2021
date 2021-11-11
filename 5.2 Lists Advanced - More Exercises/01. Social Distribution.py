populations = [int(i) for i in input().split(', ')]
minimum_salary = int(input())

if sum(populations) < minimum_salary * len(populations):
    print('No equal distribution possible')
    exit()

for i in range(len(populations)):
    biggest = max(populations)
    if populations[i] < minimum_salary:
        difference = minimum_salary - populations[i]
        populations[i] += difference
        if populations[populations.index(biggest)] - difference < minimum_salary:
            break
        else:
            populations[populations.index(biggest)] -= difference
            biggest = max(populations)
        if populations[populations.index(biggest)] < minimum_salary:
            break

print(populations)
