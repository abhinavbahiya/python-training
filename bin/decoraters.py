def mydec (func_to_be_decorated):
    def decorated_func(x, y):
        print("Some result")
        func_to_be_decorated(x, y)
        print('End')
    return  decorated_func


@mydec
def add1 (a, b):
    print(a+b)

add1(100, 200)