#we are using multiplication
def above_zero_result_decor(func):
    def get_fun_result(*args, **kwargs):
        return (func(*args, **kwargs))*(func(*args, **kwargs))
    return get_fun_result

#example of a function
@above_zero_result_decor
def f(a, b, c=1, d=2):
    return a + b + c + d

#checking the decorator
print(f(1, -2, -50))
print(f(1, 1))
