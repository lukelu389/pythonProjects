def strange_operations(sample):
    output = []
    i = 0
    while i < len(sample):
        prefix = set(sample[0:i+1])
        suffix = set(sample[i+1:len(sample)])
        output.append(len(prefix)-len(suffix))
        i+= 1

    return output


print(strange_operations([1, 2, 3, 4, 5]))
