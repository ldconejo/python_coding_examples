def newer_range(stop=5, start=0, step=1):
    i = start
    while i < stop:
        yield i
        i += step

#for value in newer_range(10):
#    print(value)