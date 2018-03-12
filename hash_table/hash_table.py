import itertools
import pprint


class ChainHashTable:
    def __init__(self, capacity=64):
        self.capacity = capacity
        self.lst = [[] for _ in range(self.capacity)]

    def __setitem__(self, key, value):
        index = hash(key) % self.capacity
        for (i, (k, _)) in enumerate(self.lst[index]):
            if k == key:
                self.lst[index][i-1] = (key, value)
                return key, value

        self.lst[index] += [(key, value)]
        return key, value

    def __getitem__(self, key):
        index = hash(key) % self.capacity
        for (k, v) in self.lst[index]:
            if k == key:
                return v

        raise ValueError("There is no {0} key in the table".format(key))

    def keys(self):
        chains = [self.lst[index] for index in range(self.capacity)]
        return [k for (k, v) in itertools.chain.from_iterable(chains)]

    def values(self):
        chains = [self.lst[index] for index in range(self.capacity)]
        return [v for (k, v) in itertools.chain.from_iterable(chains)]


class OpenHashTable:
    def __init__(self, capacity=64):
        self.capacity = capacity
        self.lst = [None for _ in range(self.capacity)]
        self.simple = self.__get_simple(self.capacity)

    def __expand(self):
        items = self.keys()
        self.capacity *= 2
        self.simple = self.__get_simple(self.capacity)
        self.lst = [None for _ in range(self.capacity)]
        for (key, value) in items:
            self.__setitem__(key, value)

    def __setitem__(self, key, value):
        base_index = hash(key) % self.capacity
        for i in range(self.capacity):
            index = (base_index + i*self.simple) % self.capacity
            if self.lst[index] is None:
                self.lst[index] = (key, value)
                return key, value
            elif self.lst[index][0] == key:
                self.lst[index] = (key, value)

        self.__expand()

    def __getitem__(self, key):
        base_index = hash(key) % self.capacity
        for i in range(self.capacity):
            index = (base_index + i*self.simple) % self.capacity
            if self.lst[index] is not None:
                if self.lst[index][0] == key:
                    return self.lst[index]

        raise ValueError("There is no {0} key in the table".format(key))

    def __get_simple(self, base):
        def check_simple(number):
            sqrt = int(number**(1/2))
            for delim in range(2, sqrt+1):
                if number % sqrt == 0:
                    return False

            return True

        for number in itertools.count(base+1):
            if check_simple(number):
                return number

    def keys(self):
        return [pair[0] for pair in self.lst if pair is not None]

    def values(self):
        return [pair[1] for pair in self.lst if pair is not None]

    def items(self):
        return [pair for pair in self.lst if pair is not None]


def main():
    cht = ChainHashTable()
    cht["key1"] = 3
    cht["key2"] = 5
    cht["key3"] = 7
    print(cht["key1"])
    print(cht["key2"])

    oht = OpenHashTable(capacity=4)
    oht["key1"] = 3
    oht["key2"] = 5
    oht["key3"] = 7
    print(oht["key1"])
    print(oht["key2"])
    print(oht["key3"])
    print(oht["key4"])


if __name__ == "__main__":
    main()