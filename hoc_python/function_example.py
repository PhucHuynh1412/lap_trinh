def my_function(food):
    for x in food:
        print(f"This is a {x}")

fruits = ["apple","banana","cherry"]
my_function(fruits)

def my_function_1(x):
    return 5*x

print(my_function_1(5))
print(my_function_1('phuc'))

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion example result")
tri_recursion(6)

