class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Sieve of Eratosthenes : Basically a better way to find primes with O(nloglogn) time complexity
        def get_prime():
            is_prime = [True] * (right + 1)
            is_prime[0] = is_prime[1] = False

            for n in range(2, int(sqrt(right)) + 1):
                if not is_prime[n]:
                    continue
                for m in range(n + n, right + 1, n):
                    is_prime[m] = False

            primes = []
            for i in range(len(is_prime)):
                if is_prime[i] and i >= left:
                    primes.append(i)

            return primes

        primes = get_prime()
        res = [-1, -1]
        diff = float('inf')
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < diff:
                diff = primes[i] - primes[i - 1]
                res = [primes[i - 1], primes[i]]
        
        return res