def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_list ():
    list_result = []
    for i in range (2, 30):
            if prime_number(i):
                  list_result.append(i) 

    return list_result

def primeX(x):
    listx = prime_list()
    return listx[x-1]
    return 0

if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29