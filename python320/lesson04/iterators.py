class Alphabet:
    def __init__(self, full_string):
        self.full_string = full_string
        self.coded_alphabet = {
            ' ': 'space',
            'a': 'a-wing',
            'b': 'b-wing',
            'c': 'corellian',
            'd': 'darth',
            'e': 'empire',
            'f': 'falcon',
            'g': 'gunship',
            'h': 'hoth',
            'i': 'insider',
            'j': 'jedi',
            'k': 'kylo',
            'l': 'lobot',
            'm': 'mandalorian',
            'n': 'new hope',
            'o': 'oscar',
            'p': 'power',
            'q': 'quinlan',
            'r': 'robot',
            's': 'storm trooper',
            't': 'taun-taun',
            'u': 'universe',
            'v': 'valorum',
            'w': 'wookie',
            'x': 'x-wing',
            'y': 'y-wing',
            'z': 'z-wing'
        }

    def __getitem__(self, index):
        return self.coded_alphabet[self.full_string[index].lower()]
    
#test = Alphabet("This is a test")
#for letter in test:
#    print(letter)

starwars_in_sequence = ['Rogue One', 'A New Hope', 'Empire Strikes Back', 'Return of the Jedi', 'The Mandalorian']
sw_iterator = iter(starwars_in_sequence)

# Making an iterator
class NewRange:
    def __init__(self, stop=5, start=0, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.stop:
            result = self.current
            self.current += self.step
            return result
        else:
            raise StopIteration
        
#for value in NewRange(10):
#    print(value)

#for value in NewRange(stop=10, start=2, step=2):
#    print(value)

def my_for(an_iterable, func):
    """
    Emulation of a for loop.
    func() will be called with each item in an_iterable
    """
    iterator = iter(an_iterable)
    while True:
        try:
            i = next(iterator)
        except StopIteration:
            break
        func(i)