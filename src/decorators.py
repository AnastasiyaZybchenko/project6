from functools import wraps


def log(filename=None):
    """
    декоратор для логирования функций используется для:
    1) проверки входных данных
    2) измерение времени работы декорируемой функции
    """

    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)

                if not filename or filename == "":
                    print(f"{func.__name__} ok")
                else:
                    with open("../logs/" + filename, "a") as file:
                        file.write(f"{func.__name__} ok\n")
            except Exception as e:
                result = None

                if not filename or filename == "":
                    print(f"{func.__name__} error: {e}. Inputs: {[*args]}{[*kwargs]}")
                else:
                    with open("../logs/" + filename, "a") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {[*args]}{[*kwargs]}\n")

            return result

        return wrapper

    return decor
