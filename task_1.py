class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.cursor = 0
        self.inner_cursor = 0
        return self

    def __next__(self):
        self.item = self.list_of_lists[self.cursor][self.inner_cursor]
        if self.inner_cursor < len(self.list_of_lists[self.cursor]):
            self.inner_cursor += 1
        else:
            self.cursor += 1
            self.inner_cursor = 0
        if self.cursor < len(self.list_of_lists):
            return self.item
        else:
            raise StopIteration



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item
    asd = list(FlatIterator(list_of_lists_1))

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()