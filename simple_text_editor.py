def simple_text_editor():
    S = "abcde"
    Q = int(input("Query: "))
    ops = [0]*Q
    last_op = [S]
    for i in range(Q):
        ops[i] = input("Operation: ")
        char = ops[i].split(" ")
        if char[0] == '1':
            S = S + char[1]
            last_op.append(S)
        elif char[0] == '2':
            S=S[:-int(char[1])]
            # S = S[:len(S) - char[1]-1]
            last_op.append(S)
        elif char[0] == '3': 
            # print(S[char[1]-1])
            print(S[int(char[1])-1])
        elif char[0] == '4':
            opr = last_op.pop()
            S=last_op[-1]

simple_text_editor()
