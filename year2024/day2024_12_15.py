def count_discrepant_up_to(N):
    """Count discrepant numbers up to N without storing results."""
    count = 0
    power_of_10 = 10  # Start rounding at 10^1

    while power_of_10 <= N:
        base_unit = power_of_10 // 10  # 10^0, 10^1, ..., determines the "step size"
        start = 45 * base_unit         # First discrepant number in the range
        end = 49 * base_unit           # Last discrepant number in the range

        # Add all numbers in the range [start, end] that are <= N
        if start <= N:
            count += max(0, min(end, N) - start + 1)

        power_of_10 *= 10  # Move to the next power of 10

    return count


def main():
    Q = int(input())  # Number of queries
    for _ in range(Q):
        N = int(input())  # Upper limit for the query
        print(count_discrepant_up_to(N))  # Count discrepant numbers dynamically


if __name__ == "__main__":
    main()
