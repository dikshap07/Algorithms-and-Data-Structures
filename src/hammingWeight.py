"""Calculate the number of "1" bits in a given binary number"""

# Optimized solution : Brian Kernighan's algorithm
# for any number n : n & (n-1)  makes rightmost 1 -> 0.


def hammingWeight(n: int) -> int:
    ones = 0

    while n != 0:
        n = n & (n - 1)
        ones += 1

    return ones


# Naive Approach : Parsing thru and keeping a counter -> O(N)


def hammingWeight(n):
    ones = 0
    print(bin(n)[2:])

    for i in str(bin(n)[2:]):
        if i == "1":
            ones += 1

    return ones


if __name__ == "__main__":
    n = 124
    print(f"HammingWeight of {n} = {hammingWeight(n)}")
