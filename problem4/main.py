def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
    
def generate_primes_grid(width, height, start):
    grid = []
    num = start+1
    max_length = len(str(start + width * height - 1))
    for _ in range(height):
        row = []
        for _ in range(width):
            while not is_prime(num):
                num += 1
            row.append(num)
            num += 1
        grid.append(row)

    result = ""
    for row in grid:
        result += " ".join([f"{x:>{max_length}}" for x in row]) + "\n"

    return result

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """