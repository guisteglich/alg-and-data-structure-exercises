def matchingStrings(strings, queries):
    c = []
    for query in queries:
        count = 0
        for string in strings:
            if string == query:
                count += 1
        c.append(count)
    return c


strings = ['aba', 'baba', 'aba', 'xzxb']        
queries = ['aba', 'xzxb', 'ab']

print(matchingStrings(strings, queries))