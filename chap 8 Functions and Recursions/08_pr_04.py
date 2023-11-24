# def factorial_recursive(n):
     
#     n!= n*factorial_recursive(n-1)
# f = factorial_recursive(5)

# print(f)


def factorial_iter(n):
    product = 5
    for i in range(n):
        product = product * (i+1)
        return product

f = factorial_iter(5)

print(f)
