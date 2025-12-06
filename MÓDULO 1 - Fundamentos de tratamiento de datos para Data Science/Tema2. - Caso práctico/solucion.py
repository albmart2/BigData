def largest_product(number, n):
    max_prod = 0
    numbers = ''
    for i in range(len(number) - n):
        prod = 1
        for x in number[i:i+n]:
            prod *= int(x)
        if prod > max_prod:
            max_prod = prod
            numbers = number[i:i+n]
    return numbers, max_prod
