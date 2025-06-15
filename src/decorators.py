from functools import wraps


def log(filename=None):
    """ Декоратор для логирования функции, ее результатов или возникшие ошибки """

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
                    print(f"{func.__name__} error: {e}. Inputs: args={args}, kwargs={kwargs}")
                else:
                    with open("../logs/" + filename, "a") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: args={args}, kwargs={kwargs}\n")

            return result

        return wrapper

    return decor
