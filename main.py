"""
ccc s3 possible integer related problems:

Balanced Split Problem
Given an array of N integers, check if it's possible to partition them into groups with equal sum.
Concepts: Prefix sums, binary search, set.

Jumping Frog Game
Given an integer sequence, find the longest subsequence where each number is reachable by jumping +1 or -1.
Concepts: Dynamic programming, sliding window, greedy.

Integer Divisibility Chain
Find the longest sequence where each number a[i] is a divisor of a[i+1].
Concepts: Sorting, graph traversal.

Sum to Target
Given an array and K, determine if a subset of elements sums to exactly K.
Concepts: Bitmasking, DP.

GCD Graph
Construct a graph where nodes are numbers, and an edge exists if gcd(a, b) > 1.
Find the smallest connected component.
Concepts: DSU (Disjoint Set Union), number theory.

Constructing a Magic Square
Construct an NxN matrix where each row, column, and diagonal sums to the same number.
Concepts: Permutations, simulation.

Integer Partitioning with Constraints
Given N, split it into positive integers that sum to N but with additional rules (e.g., no consecutive equal values).
Concepts: Recursion, memoization.

Minimum Swaps to Sort an Array
Find the minimum number of adjacent swaps to sort an array.
Concepts: Cycle decomposition, greedy.

Transform One Integer to Another
Convert A to B using allowed operations (+2, *3, -1). Find the minimum steps.
Concepts: BFS (Shortest path in an implicit graph).

Number Reconstruction from Modulo Queries
Given an array and queries of the form "x mod k = r", reconstruct the hidden numbers.
Concepts: CRT (Chinese Remainder Theorem), constructive math.

"""

# Senior1 - simple math - goal AC
# Senior2 - string manipulation - goal AC
# Senior3 - constructive - goal High Partial
# Senior4 - dp - goal - Partial
# Senior5 - graph theory - first subtask