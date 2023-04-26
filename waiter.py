def waiter(number, q):
    lower = 2
    upper = 10000
    primes = [i for i in range(lower, upper + 1) if all(i % j != 0 for j in range(2, i))]
    
    answers = []
    a_aux = number
    for i in primes[0:q]:
        # b =[]
        a = a_aux
        a_aux = []
        for elem in a:
            if elem % i == 0:
                # b.insert(0, elem)
                answers.append(elem)
            else:
                a_aux.insert(0, elem)
    for e in a_aux[::-1]:
        answers.append(e)

    return answers

number = [3, 3, 4, 4, 9]
q = 2

print(waiter(number, q))

n = [3, 4, 7, 6, 5]

print(waiter(n, 1))