class MultiConstructor:

    def __init__(self, **kwargs) -> None:
        if "number" in kwargs:
            self.__init__number()
        elif "name" in kwargs:
            self.__init__person()


    def __init__number(self):
        print("Calling the number constructor")

    def __init__person(self):
        print("Calling the person constructor")

