try:
    number = int(input("enter the number: "))
    print(10 / number)
except ZeroDivisionError:
    print("cannot divide by zero")
except Exception:
    print("something went wrong")
