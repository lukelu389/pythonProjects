from queue import PriorityQueue


def kClosest(points, k):
    pq = PriorityQueue()
    output = []
    for i in points:
        temp = (i[0] ** 2 + i[1] ** 2)
        pq.put((temp, i))

    for j in range(k):
        output.append(pq.get()[1])

    return output



print(kClosest([[1,3],[-2,2]], 1))
