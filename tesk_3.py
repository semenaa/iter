class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        # Список курсоров на каждом уровне вложенности, изначально содержит только нулевой элемент верхнего списка
        self.depth_cursor = [0]
        return self

    def __next__(self):
        return self.get_list_item(self.list_of_lists)

    def get_list_item(self, obj):
        if isinstance(obj, list):
            # Если достигнут последний элемент данного списка
            if self.depth_cursor[-1] == len(obj) and len(obj) > 0:
                # Удалить последний элемент списка курсоров и увеличить предыдущий на один
                self.depth_cursor.pop(-1)
            self.depth_cursor[-1] += 1



def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()