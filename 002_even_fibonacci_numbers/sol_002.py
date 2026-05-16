# https://projecteuler.net/problem=2
import math
import time

def main():
    start_time = time.perf_counter()
    sol = fibonacci_naive()
    end_time = time.perf_counter()

    execution_time = end_time - start_time
    print(f"Solution: {sol}, execution time: {execution_time} s")
 
    start_time = time.perf_counter()
    sol = fibonacci_v2()
    end_time = time.perf_counter()

    execution_time = end_time - start_time
    print(f"Solution: {sol}, execution time: {execution_time} s")

    return

def fibonacci_naive():
    sol = 2
    def run_fib(n1, n2):
        nonlocal sol

        new_n2 = n1 + n2
        new_n1 = n2

        if new_n2 > 4e6:
            return

        if new_n2 % 2 == 0:
            sol += new_n2
        return run_fib(new_n1, new_n2)
    
    run_fib(1, 2)
    return sol

def fibonacci_v2():
    # Binet equation: F(n) = phi^n / sqrt(5) - (1-phi^n) / sqrt(5)
    phi = (1+math.sqrt(5))/2

    # Fib always O, O, E, O, O, E ...
    n = 3
    sol = 0

    val = round(phi**n/math.sqrt(5))    # |(1-phi^3)| = 0.236 < 0.5
    while val < 4e6:
        sol += val
        n += 3
        val = round(phi**n/math.sqrt(5)) 
    return sol

if __name__ == '__main__':
    main()  