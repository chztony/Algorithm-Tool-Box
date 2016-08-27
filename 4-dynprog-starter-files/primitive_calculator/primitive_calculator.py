# Uses python3
import sys

def optimal_sequence_original(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def optimal_sequence(n):
    sequence = []
    minnum = list(0 for _ in range(n+1))

    minnum[0] = 0
    for i in range(1, n+1):
        minnum[i] = n+10
        if i == 1:
            minnum[i] = 0
        else:
            if i % 3 == 0:
                minvalue = minnum[i//3] + 1
            elif i % 3 == 1:
                minvalue = minnum[i//3] + 2
            else:
                minvalue = minnum[i//3] + 3
            if minvalue < minnum[i]:
                minnum[i] = minvalue

            if i % 2 == 0:
                minvalue = minnum[i//2] + 1
            else:
                minvalue = minnum[i//2] + 2
            if minvalue < minnum[i]:
                minnum[i] = minvalue

            minvalue = minnum[i-1]+1
            if minvalue < minnum[i]:
                minnum[i] = minvalue

    sequence.append(n)
    while n >= 1:
        route = min(minnum[n//3], minnum[n//2], minnum[n-1])
        if route == minnum[n//3]:
            if n % 3 == 2:
                n = n//3
                sequence.append(n*3+1)
                sequence.append(n*3)
                sequence.append(n)
            elif n % 3 == 1:
                n = n//3
                sequence.append(n*3)
                sequence.append(n)
            else:
                n = n//3
                sequence.append(n)
        elif route == minnum[n//2]:
            if n % 2 == 1:
                n = n//2
                sequence.append(n*2)
                sequence.append(n)
            else:
                n = n//2
                sequence.append(n)
        else:
            n = n - 1
            sequence.append(n)
        print(n)
    return list(reversed(sequence)), minnum


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
