# questionNumber = int(input())
# riderNum = int(input())
# dRiders = [int(i) for i in input().split()]
# pRiders = [int(i) for i in input().split()]
#
# dRiders.sort()
# output = 0
#
# if questionNumber == 1:
#     pRiders.sort()
#     for i in range(riderNum):
#         output += max(dRiders[i], pRiders[i])
#
# else:
#     pRiders.sort(reverse=True)
#     for i in range(riderNum):
#         output += max(dRiders[i], pRiders[i])
#
# print(output)

numPie = int(input())
people = int(input())

piemap = dict()


def pie(pies, people):
    if pies < people:
        return 0

    if people == pies or people == 1:
        return 1

    if (pies, people) in piemap:
        return piemap[(pies, people)]
    piemap[(pies, people)] = pie(pies - 1, people - 1) + pie(pies - people, people)
    return piemap[(pies, people)]


print(pie(numPie, people))

