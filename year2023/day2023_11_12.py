from queue import PriorityQueue
# def canFinish(numCourses, prerequisites):
#     if numCourses <= 1:
#         return True
#
#     if len(prerequisites) == 0 or len(prerequisites[0]) == 0:
#         return True
#
#     hierarchy = {}
#     cue = []
#     not_taken = numCourses
#
#     for i in range(numCourses):
#         hierarchy[i] = []
#
#     for j in prerequisites:
#         hierarchy[j[0]].append(j[1])
#
#     for key, value in hierarchy.items():
#         if len(value) == 0:
#             cue.append(key)
#             not_taken -= 1
#
#     while len(cue) > 0:
#         temp = cue.pop()
#
#         for value in hierarchy.values():
#             if temp in value:
#                 value.remove(temp)
#                 if len(value) == 0:
#
#                     cue.pop(temp)
#                     not_taken -= 1
#
#     return not_taken == 0
#
#
# print(canFinish(2, [[1, 0]]))



