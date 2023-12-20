class Vector:
    def __init__(self, x, y):
        print("Running the init method")
        self.x = x
        self.y = y
        print(x, y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    # Other math magic methods:
    # __sub__, __mul__, __abs__

if __name__ == "__main__":
    vector_A = Vector(3, 5)