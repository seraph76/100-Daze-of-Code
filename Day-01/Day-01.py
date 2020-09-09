"""
CREATED: 9/8/2020 - 7:29 PM
@AUTHOR: Seraph-LXXVI
"""
# Without using any string methods, Print a list of integers from 1 through N as a string, without spaces. Example:
# INPUT: n = 5
# OUTPUT: 12345

def solve1():
    n = int(input())
    res = [str(i) for i in range(1, n+1)]
    return ''.join(res)

print(solve1())

print(solve1())
