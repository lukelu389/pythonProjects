def fruits_in_baskets(sample):
    start = 0
    most_fruits = 0
    baskets = {}
    for end in range(len(sample)):
        if sample[end] not in baskets:
            baskets[sample[end]] = 1

        else:
            baskets[sample[end]] += 1

        while len(baskets) > 2:
            fruit = sample[start]
            start += 1
            baskets[fruit] -= 1
            if baskets[fruit] == 0:
                baskets.pop(fruit)

        if sum(baskets.values()) > most_fruits:
            most_fruits = sum(baskets.values())

    return most_fruits


print(fruits_in_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
