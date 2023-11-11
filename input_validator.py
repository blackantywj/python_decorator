'''
这个封装函数根据指定的条件或数据类型验证一个函数的输入参数。它可以用来确保输入数据的正确性和一致性。
(另一种方法是在我们想要验证输入数据的函数内创建无数的assert行，来实现这一目的。)
为了给装饰添加验证，我们需要用另一个函数来包装装饰函数，该函数接收一个或多个验证函数作为参数。这些验证函数负责检查输入值是否符合某些标准或条件。
validate_input函数本身现在作为一个装饰器。在封装函数中，input和keyword的参数会根据提供的验证函数进行检查。如果任何参数没有通过验证，就会引发一个 "ValueError"，并显示无效参数的信息。
'''

def validate_input(*validations):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i, val in enumerate(args):
                if i < len(validations):
                    if not validations[i](val):
                        raise ValueError(f"Invalid argument: {val}")
            for key, val in kwargs.items():
                if key in validations[len(args)]:
                    if not validations[len(args):][key](val):
                        raise ValueError(f"Invalid argument: {Key}={val}")
            return func(*args, **kwargs)
        return wrapper
    return decorator