def solve(N: int, X: list[int]) -> int:
    from collections import Counter
    #N: the number of faces on the die
    #X: the list of numbers on each face of the die

    element_counts = Counter(X)
    sortedList = sorted(X, key=lambda x: element_counts[x], reverse=True)
    noDuplSortedList = list(dict.fromkeys(sortedList))
 
    answer = 0
    currentTotal = 0
    lowestTotal = 1000000000000000

    for i in range(len(noDuplSortedList)):
        currentTotal = 0
        for x in range(N):
            if X[x] != noDuplSortedList[i]: #if array element doesnt match cancel value
                currentTotal += X[x]
        if (currentTotal < lowestTotal):
            lowestTotal = currentTotal
            answer = noDuplSortedList[i]
    return answer

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X = [int(x) for x in input().strip().split(' ')]
        print(solve(N, X))

if __name__ == '__main__':
    main()
