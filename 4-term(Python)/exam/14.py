class BaseSingle(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class Singleton(BaseSingle):
    def __init__(self):
        print(228)


a = Singleton()
b = Singleton()

print(a == b)
