def down_binary(target):
    left = 0
    right = len(cards) -1

    while left <= right:
        mid = (left + right) //2
        if cards[mid] >= target:
            right = mid-1
        elif cards[mid] < target:
            left = mid + 1
    return left


def up_binary(target):
    left = 0
    right = len(cards) - 1

    while left <= right:
        mid = (left + right) // 2
        if cards[mid] > target:
            right = mid - 1
        elif cards[mid] <= target:
            left = mid + 1
    return left


import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
targets = list(map(int, input().split()))

for i in range(m):
    result = up_binary(targets[i]) - down_binary(targets[i])
    print(result, end = ' ')
