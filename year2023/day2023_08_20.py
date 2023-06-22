def distinct_average(sample):
    sample.sort()
    temp_average = set()
    i = 0
    j = len(sample) - 1
    while i != j:
        temp_average.add((sample[i] + sample[j]) / 2)
        i += 1
        j -= 1

    return len(temp_average)


print(distinct_average([1, 100]))
