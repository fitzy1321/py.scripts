class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.data = "Some Data"


if __name__ == "__main__":
    singleton1 = Singleton
    singleton2 = Singleton

    print(
        f"Are these 2 objects, {singleton1=}, {singleton2=}, the same?",
        "yes" if singleton1 is singleton2 else "no",
    )
