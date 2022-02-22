class CustomRange:
    def __init__(self, start, end, increment):
        self.current = start
        self.end = end
        self.increment = increment

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            output = self.current
            self.current += self.increment
            return output
        else:
            raise StopIteration()

class OtherRange:
    def __init__(self, start, end, increment):
        self.current = start
        self.end = end
        self.increment = increment

    def iter(self):
        return self

    def next(self):
        if self.current < self.end:
            output = self.current
            self.current += self.increment
            return output
        else:
            raise StopIteration()

if __name__ == "__main__":
    test_range = CustomRange(5, 30, 3)
    print(f"First element: {next(test_range)}")
    for element in test_range:
        print(element)

    print('-------------------------')
    test_range = OtherRange(5, 30, 3)
    print(f"First element: {next(test_range)}")
    for element in iterator(test_range):
        print(element)