def fibonacci(x):
    num_list = [0, 1]
    for i in range (2, x + 1):
        next_ele = num_list [-1] + num_list[-2]
        num_list.append(next_ele)
    
    if x < 0 or x >= len(num_list):
        return None
    
    return num_list[x]


if __name__ == "__main__":
    print(fibonacci(0))  # 0
    print(fibonacci(2))  # 1
    print(fibonacci(9))  # 34
    print(fibonacci(10)) # 55
    print(fibonacci(12)) # 144