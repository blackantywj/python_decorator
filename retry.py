'''
这个封装器会重试一个函数的执行，并在重试之间有一定的延迟。在处理网络或API调用时，它可能会因为临时问题而偶尔失败，因此很有用。

为了实现这一点，我们可以为我们的装饰器定义另一个包装函数，与我们之前的例子类似。然而，这次我们不是将验证函数作为输入变量，而是传递特定的参数，如max_attemps和delay。

当装饰函数被调用时，wrapper函数被调用。它记录了尝试的次数（从0开始）并进入一个while循环。循环尝试执行装饰后的函数，如果成功，立即返回结果。然而，如果发生异常，它就会增加尝试计数器，并打印出一条错误信息，指出尝试次数和发生的具体异常。然后，它使用time.sleep等待指定的延迟，然后再次尝试该函数。
'''
import time


def retry(max_attempts, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed: {e}")
                    time.sleep(delay)
            print(f"Function failed after {max_attempts} attempts")
        return wrapper
    return decorator