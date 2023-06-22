def average_of_k(sample, k):
    temp = sample[:k]
    s = sum(temp)
    result = [s/k]
    for i in range(k, len(sample)):
        temp = temp[1:k] + [sample[i]]
        result.append(sum(temp)/k)

    return result


print(average_of_k([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))

