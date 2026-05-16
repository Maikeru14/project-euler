# https://projecteuler.net/problem=1
import time

def main():
    multiples = [3, 5]
    N = 1000

    start_time = time.perf_counter()
    sol  = run_computation_simple(N, multiples)
    end_time = time.perf_counter()

    execution_time = end_time - start_time
    print(f"Solution: {sol}, execution time: {execution_time} s")

    start_time = time.perf_counter()
    sol  = analytical_sol()
    end_time = time.perf_counter()

    execution_time = end_time - start_time
    print(f"Solution: {sol}, execution time: {execution_time} s")

    return

def run_computation_simple(N: int, multiples: list[int]):
    return sum([k for k in range(N) if int(any(k % m == 0 for m in multiples)) ])

def analytical_sol():
    GCM = 990   # greatest common multiplier of 3 and 5 below 1000
    a = 993 + 995 + 996 + 999     # valid numbers from 990 to 999
    
    n_three_div = 330   # 990 / 3 = 330
    b = n_three_div*(GCM+3)/2

    n_five_div = 198
    c = n_five_div*(GCM+5)/2

    n_fifteen_div = 66
    d = n_fifteen_div*(GCM+15)/2
    return a+b+c-d

if __name__ == '__main__':
    main()