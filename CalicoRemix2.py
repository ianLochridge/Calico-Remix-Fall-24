
def solve(S: str) -> str:
    num = int(S)
    ans = ''
    if num < 10:
        return 'haha good one'
    elif num > 170:
        return 'canceled'
    
    num = num//10
    for x in range(num):
        ans += 'berkeley' 
    return ans + 'time'

def main():
    T = int(input())
    for _ in range(T):
        S = input()
        print(solve(S))

if __name__ == '__main__':
    main()