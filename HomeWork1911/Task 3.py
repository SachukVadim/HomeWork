class Iterator:
    def __init__(self, my_list: list):
        self.list = my_list

    def __iter__(self):
        self.reversed = self.list
        return self

    def __next__(self):
        if not self.reversed:
            raise StopIteration
        else:
            return self.reversed.pop()


list = [1, 2, 3, 4, 5, 67, 8, 76, 5, 4, 678, 7, 6, 5]
for value in Iterator(list):
    print(value)
