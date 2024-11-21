
def solve(S: str) -> str:
   #struc = optional cons, mandatory vow, optional n
    wordContained = lambda s, l: any(map(lambda x: x in s, l))  
    illegalSegments = ['wu', 'wo', 'ji', 'ti', 'nn', 'nm']
    vowels = 'aeiou'
    consts = 'mnptkswjl'
    vowelCount = 0
    vowelsPassed = 1
    
    if wordContained(S, illegalSegments): #illegal segment present -> ike
        return 'ike'

    for j in range(len(S)):
        if S[j] in vowels:
            vowelCount = vowelCount+1

    if len(S) < 1: #impossible length word -> ike
        return 'ike'

    if len(S) > 3*vowelCount: #impossible length word -> ike
        return 'ike'
    
    for x in range(len(S)):
        if S[x] in vowels:
            if (x-1) >= 0: #before char exists 
                if S[x-1] in vowels: #before char is a vowel -> ike
                    return 'ike'
                if S[x-1] not in consts: #before char is a banned const -> ike
                    return 'ike'
        
            if (x+1) < len(S): #after char exists
                if S[x+1] in vowels: #after char is a vowel -> ike
                    return 'ike'
                if S[x+1] not in consts: #after char is a banned const -> ike
                    return 'ike'
            
            if vowelsPassed == vowelCount:
                if (x+1) < len(S): #after char exists
                    if S[x+1] != 'n': #after char on 1 syllable char doesnt = n -> ike
                        return 'ike'
            vowelsPassed = vowelsPassed+1
                 
    return 'pona'         
                
def main():
    T = int(input())
    for _ in range(T):
        S = input()
        print(solve(S))

if __name__ == '__main__':
    main()