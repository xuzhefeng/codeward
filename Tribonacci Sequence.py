def tribonacci(signature, n):
    a,b,c = signature
    result_list = [a,b,c]
    if n == 0:
        return []
    if n in range(1,4):
        return result_list[0:n]
    for i in range(n - 3):
        result_list.append(a+b+c)
        a,b,c = b,c,a+b+c
    return result_list
print(tribonacci([1,1,1],3))


