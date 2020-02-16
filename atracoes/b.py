def f1():
    try:
        return 1
    finally:
        return 2


x = f1()
print(x)