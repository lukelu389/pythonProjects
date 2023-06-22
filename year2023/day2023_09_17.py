def intersected_parking(sample):
    sample.sort()
    start = sample[0][0]
    end = sample[0][1]
    s = 0
    for i in sample:
        if i[0] < start and i[1] > end:
            start = i[0]
            end = i[1]

        elif i[1] > end and i[0] < end:
            end = i[1]

        elif i[0] > start:
             s += (end - start + 1)
             start = i[0]
             end = i[1]


        elif i[0] < start and i[1] > start:
            start = i[0]

    s += (end - start) + 1
    return s


print(intersected_parking([[1, 3], [5, 8]]))

