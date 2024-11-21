def solve() -> None:
   
    feed(6)
    feed(3) 
    feed(12)
    feed(9) 
    
    poopInt = poop()

    if poopInt == 6:
        if guess('queueon') == 'WRONG_ANSWER':
            exit()
        else: 
            return 'queueon'
    elif poopInt == 12:
        if guess('heapeon') == 'WRONG_ANSWER':
            exit()
        else:  
            return 'heapeon'   
    elif poopInt == 9:
        if guess('stackeon') == 'WRONG_ANSWER':
            exit()
        else:
            return 'stackeon'
    

def feed(i: int) -> str:
    """
    Feed a number to the Datamon. Returns OK if successful.
    """
    print('feed', i, flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()
    return response


def poop() -> int:
    """
    Get the Datamon to poop out a number. Returns the number pooped out.
    """
    print('poop', flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()
    return int(response)


def guess(s: str) -> str:
    """
    Guess the species of the Datamon and end this test case. Returns CORRECT if
    the guess is correct. Exits otherwise.
    """
    print('guess', s, flush=True)
    response = input()
    if response == 'WRONG_ANSWER':
        exit()
    return response


def main():
    T = int(input())
    for _ in range(T):
        solve()


if __name__ == '__main__':
    main()
