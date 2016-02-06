
from scipy.special import comb

class Animal:
    def __init__(self, size):
        self.size = size

    def grow(self ,rate ,duration):
        a=rate* self. size* duration
        return a

def main():
    size = 3
    rate = 2
    duration = 10
    chien = Animal(size)
    newsize = chien.grow(rate, duration)


if __name__ == "__main__":
    main()
