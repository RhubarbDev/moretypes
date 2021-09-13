class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


class Char:
    def __init__(self, char: str):
        if len(char) == 1:
            self._c = char
        else:
            raise TypeError()

    def __str__(self):
        return self._c

    @property
    def char(self):
        return self._c

    @char.setter
    def char(self, char):
        if len(char) == 1:
            self._c = char
        else:
            raise TypeError()
