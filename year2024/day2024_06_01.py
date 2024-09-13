# 738
from collections import defaultdict


def monotoneIncreasingDigits(n):
    # Single digit case
    if n < 10:
        return n

    # Convert the number into a list of integers
    l = []
    for _, c in enumerate(str(n)):
        l.append(int(c))
    n = len(l)

    # Traverse from right to left
    for i in range(n - 1, 0, -1):
        if l[i] < l[i - 1]:
            l[i - 1] -= 1
            for i in range(i, n):
                l[i] = 9

    return int("".join([str(x) for x in l]))


# 131


def partition(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                backtrack(end, path + [s[start:end]])

    result = []
    backtrack(0, [])
    return result

    # 332, 56, 37
    #      v


def merge(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    start, end = intervals[0]

    for interval in intervals:
        if interval[0] <= end:
            end = max(end, interval[1])
        else:
            merged.append([start, end])
            start, end = interval

    merged.append([start, end])
    return merged


def findItinerary(tickets):
    graph = defaultdict(list)

    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)

    itinerary = []

    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop())
        itinerary.append(airport)

    dfs("JFK")

    return itinerary[::-1]


print(findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))


# ["JFK","MUC","LHR","SFO","SJC"]

# 210, 802


def findOrder(numCourses, prerequisites):
    prereq = {c: [] for c in range(numCourses)}
    for crs, pre in prerequisites:
        prereq[crs].append(pre)

    output = []
    visit, cycle = set(), set()

    def dfs(crs):

        if crs in cycle:
            return False

        if crs in visit:
            return True

        cycle.add(crs)

        for pre in prereq[crs]:
            if not dfs(pre):
                return False

        cycle.remove(crs)

        visit.add(crs)
        output.append(crs)
        return True

    for c in range(numCourses):
        if not dfs(c):
            return []
    return output


def eventualSafeNodes(graph):
    res = []
    visited = {}

    def dfs(node):
        if node in visited:
            return visited[node]

        visited[node] = True

        for nei in graph[node]:
            if dfs(nei):
                return True

        visited[node] = False

    for i in range(len(graph)):
        if not dfs(i):
            res.append(i)

    return res

# computer science, computer engineering, software engineering, which requires the highest score

