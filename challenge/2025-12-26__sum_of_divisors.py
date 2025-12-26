def sum_divisors(n):
    # Handle the edge case for 1, as 1 only has one divisor
    if n == 1:
        return 1
    
    # We start our sum with 1 and n because they are always divisors
    total_sum = 1 + n
    
    # Now we only need to check numbers from 2 up to n // 2
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            total_sum += i
            
    return total_sum