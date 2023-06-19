def lonelyinteger(a):
    for valor in a:
        if a.count(valor) == 1:
            return valor
    
    return None 
    
a1 = [0, 0, 1, 2, 1]
a2 = [1, 1, 2]
print(lonelyinteger(a1))
print(lonelyinteger(a2))