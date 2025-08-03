def greeting(greet):
    print(f"Good {greet}")


greeting("Morning")


def calculate_sum(*args):
    initial_sum = 0
    for item in args:
        initial_sum += item
    return initial_sum


result = calculate_sum(1, 2, 3, 4, 5)
print(result)
