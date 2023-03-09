def isWinner(x, nums):
        winners = []  # list to keep track of winners of each round
        for n in nums:
            primes = sieve_of_eratosthenes(n)  # generate list of primes up to n
             turn = 0  # 0 for Maria, 1 for Ben
             remaining = set(range(2, n+1))  # set of remaining numbers to choose from
             while remaining:
             # find largest prime in remaining set                                      prime = max(p for p in primes if p in remaining)
             # remove prime and its multiples from remaining set                        remaining -= set(range(prime, n+1, prime))
             # check if player cannot make a move
             if not any(p in primes and p in remaining for p in range(2, prime)):
                 winners.append("Maria" if turn == 0 else "Ben")
                 break
             # switch turns
             turn = 1 - turn
         else:
             winners.append(None)  # game ended in a tie
    # count number of wins for each player
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")
    # determine winner of all rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False

    return [i for i in range(n+1) if primes[i]]
